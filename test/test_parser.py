import unittest
from src.parser import MarkdownParser


class TestMarkdownParser(unittest.TestCase):
    def setUp(self):
        self.parser = MarkdownParser()

    def test_headers(self):
        markdown = "# Header 1\n## Header 2"
        result = self.parser.parse(markdown)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['type'], 'h1')
        self.assertEqual(result[1]['type'], 'h2')

    def test_lists(self):
        markdown = "- Item 1\n- Item 2"
        result = self.parser.parse(markdown)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['type'], 'ul')
        self.assertEqual(result[1]['type'], 'ul')

    def test_formatting(self):
        markdown = "**bold** *italic*"
        result = self.parser.parse(markdown)
        self.assertEqual(len(result), 1)
        self.assertIn({'type': 'bold', 'content': 'bold'}, result)
        self.assertIn({'type': 'italic', 'content': 'italic'}, result[0]['content'])


if __name__ == '__main__':
    unittest.main()
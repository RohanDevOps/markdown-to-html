import unittest
from src.converter import MarkdownConverter


class TestMarkdownConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MarkdownConverter()

    def test_headers(self):
        markdown = "# Header 1\n## Header 2\n### Header 3"
        expected = "<h1>Header 1</h1>\n<h2>Header 2</h2>\n<h3>Header 3</h3>"
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_lists(self):
        markdown = "- Item 1\n- Item 2\n1. Item 1\n2. Item 2"
        expected = "<ul><li>Item 1</li>\n<li>Item 2</li></ul>\n<ol><li>Item 1</li>\n<li>Item 2</li></ol>"
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_formatting(self):
        markdown = "**bold** *italic* `code`"
        expected = "<p><strong>bold</strong> <em>italic</em> <code>code</code></p>"
        self.assertEqual(self.converter.convert(markdown), expected)


if __name__ == '__main__':
    unittest.main()
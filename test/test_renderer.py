import unittest
from src.renderer import HTMLRenderer


class TestHTMLRenderer(unittest.TestCase):
    def setUp(self):
        self.renderer = HTMLRenderer()

    def test_header_rendering(self):
        document = [{'type': 'h1', 'content': 'Header'}]
        self.assertEqual(self.renderer.render(document), '<h1>Header</h1>')

    def test_list_rendering(self):
        document = [
            {'type': 'ul', 'content': 'Item 1'},
            {'type': 'ul', 'content': 'Item 2'}
        ]
        expected = '<ul><li>Item 1</li>\n<li>Item 2</li></ul>'
        self.assertEqual(self.renderer.render(document), expected)

    def test_formatting_rendering(self):
        document = [
            {'type': 'paragraph', 'content': [
                {'type': 'bold', 'content': 'bold'},
                ' ',
                {'type': 'italic', 'content': 'italic'}
            ]}
        ]
        expected = '<p><strong>bold</strong> <em>italic</em></p>'
        self.assertEqual(self.renderer.render(document), expected)


if __name__ == '__main__':
    unittest.main()
import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, url="https://example.com")
        self.assertEqual(repr(node), "TextNode(TEXT='This is a text node', TYPE=BOLD, URL='https://example.com')")

    def test_repr_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(TEXT='This is a text node', TYPE=BOLD, URL=None)")

    def test_eq_different_url(self):
        node1 = TextNode("another text node", TextType.ITALIC, url="www.testequal1.com")
        node2 = TextNode("another text node", TextType.ITALIC, url="www.testnequal1.com")
        self.assertNotEqual(node1, node2)

    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.to_html()
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_bold_to_html(self):
        node = TextNode("Bold text", TextType.BOLD)
        self.assertEqual(node.to_html().to_html(), "<b>Bold text</b>")

    def test_italic_to_html(self):
        node = TextNode("Italic text", TextType.ITALIC)
        self.assertEqual(node.to_html().to_html(), "<i>Italic text</i>")

    def test_code_to_html(self):
        node = TextNode("code()", TextType.CODE)
        self.assertEqual(node.to_html().to_html(), "<code>code()</code>")

    def test_link_to_html(self):
        node = TextNode("Click", TextType.LINK, url="https://example.com")
        self.assertEqual(node.to_html().to_html(), '<a href="https://example.com">Click</a>')

    def test_image_to_html(self):
        node = TextNode("My image", TextType.IMAGE, url="https://example.com/img.png")
        self.assertEqual(node.to_html().to_html(), '<img src="https://example.com/img.png" alt="My image">My image</img>')


if __name__ == "__main__":
    unittest.main()
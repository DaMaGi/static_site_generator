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
        node2 = TextNode("another textnode", TextType.ITALIC, url="www.testnequal1.com")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
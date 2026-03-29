import unittest
from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_init(self):
        node = HtmlNode(tag="div", value="Hello", children=[], props={"class": "my-class"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "my-class"})

    def test_repr(self):
        node = HtmlNode(tag="p", value="Paragraph", children=[], props={"id": "para1"})
        expected_repr = "Tag: p, \nValue: Paragraph, \nChildren: [], \nProperties:  id=\"para1\""
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HtmlNode(props={"class": "my-class", "id": "my-id"})
        expected_props_html = ' class="my-class" id="my-id"'
        self.assertEqual(node.props_to_html(), expected_props_html)

if __name__ == "__main__":
    unittest.main()
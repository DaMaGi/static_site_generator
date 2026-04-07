import unittest
from htmlnode import HtmlNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_init(self):
        node = HtmlNode(tag="div", value="Hello", children=[], props={"class": "my-class"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "my-class"})

    def test_repr(self):
        node = HtmlNode(tag="p", value="Paragraph", children=[], props={"id": "para1"})
        expected_repr = "Tag: p, \nValue: Paragraph, \nChildren: [], \nProperties: id=\"para1\""
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HtmlNode(props={"class": "my-class", "id": "my-id"})
        expected_props_html = ' class="my-class" id="my-id"'
        self.assertEqual(node.props_to_html(), expected_props_html)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_span_with_props(self):
        node = LeafNode('span', 'This is a span, not spam!', props={'class': 'highlight', 'style': 'color: red;'})
        self.assertEqual(node.to_html(), '<span class="highlight" style="color: red;">This is a span, not spam!</span>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Just some text without a tag.")
        self.assertEqual(node.to_html(), "Just some text without a tag.")

    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode().to_html()


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_no_children(self):
        node1 = ParentNode("div", None, props={"class": "my-class"})
        self.assertRaises(ValueError, node1.to_html)

if __name__ == "__main__":
    unittest.main()
import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_eq(self):
        properalily = 'properly'
        test_text = f"This is some **markdown** text meant to _ensure all text styles_** are** being rendered to **HTML** `all {properalily}`. There is still no support for [nested styles](https://www.istockphoto.com/photos/birds-nest-with-eggs), but it even supports images ![like this](https://www.istockphoto.com/photos/birds-nest-with-eggs)."
        output = [
            TextNode("This is some ", TextType.TEXT),
            TextNode("markdown", TextType.BOLD),
            TextNode(" text meant to ", TextType.TEXT),
            TextNode("ensure all text styles", TextType.ITALIC),
            TextNode(" are", TextType.BOLD),
            TextNode(" being rendered to ", TextType.TEXT),
            TextNode("HTML", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("all properly", TextType.CODE),
            TextNode(". There is still no support for ", TextType.TEXT),
            TextNode("nested styles", TextType.LINK, "https://www.istockphoto.com/photos/birds-nest-with-eggs"),
            TextNode(", but it even supports images ", TextType.TEXT),
            TextNode("like this", TextType.IMAGE, "https://www.istockphoto.com/photos/birds-nest-with-eggs"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(test_text), output)
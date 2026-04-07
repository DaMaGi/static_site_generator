from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    IMAGE = 5
    LINK = 6

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True

    def __repr__(self):
        return f"TextNode(TEXT={self.text!r}, TYPE={self.text_type.name}, URL={self.url!r})"

    def to_html(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(value=self.text)
            case TextType.BOLD:
                return LeafNode('b', self.text)
            case TextType.ITALIC:
                return LeafNode('i', self.text)
            case TextType.CODE:
                return LeafNode('code', self.text)
            case TextType.LINK:
                if not self.url:
                    raise ValueError("URL is required for link text nodes")
                return LeafNode('a', self.text, props={'href': self.url})
            case TextType.IMAGE:
                if not self.url:
                    raise ValueError("URL is required for image text nodes")
                return LeafNode('img', self.text, props={'src': self.url, 'alt': self.text})
            case _:
                raise ValueError(f"Unsupported TextType: {self.text_type}")

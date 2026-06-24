from __future__ import annotations
from enum import Enum
from leafnode import LeafNode

# text (plain)
# **Bold text**
# _Italic text_
# `Code text`
# Links, in this format: [anchor text](url)
# Images, in this format: ![alt text](url)


class TextType(Enum):
    PLAIN = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6


class TextNode:

    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text: str = text
        self.text_type: TextType = text_type
        self.url = url

    def text_node_to_html_node(text_node: TextNode) -> LeafNode:

        if text_node.text_type == TextType.PLAIN:
            return LeafNode(None, text_node.text)

        if text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)

        if text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)

        if text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)

        if text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})

        if text_node.text_type == TextType.IMAGE:
            return LeafNode(
                "img", "", {"src": text_node.url, "alt": text_node.text})

        raise Exception("Type of this text node is not supprted")

    def __eq__(self, other) -> bool:
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

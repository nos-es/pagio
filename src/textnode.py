from enum import Enum

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

    def __eq__(self, other) -> bool:
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

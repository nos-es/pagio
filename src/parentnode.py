from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: list[HTMLNode],
            props: dict[str, str] | None = None):

        super().__init__(tag=tag, children=children, props=props)

    def to_html(self) -> str:

        if self.tag is None or self.tag == "":
            raise ValueError("Tag has no value")

        if self.children is None:
            raise ValueError("Children is missing")

        for child in self.children:
            return f"<{self.tag}>{child.to_html()}{self.value}</{self.tag}>"

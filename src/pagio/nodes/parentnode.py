from pagio.nodes.htmlnode import HTMLNode


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

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props}"

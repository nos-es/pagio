from pagio.nodes.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str | None,
            value: str,
            props: dict[str, str] | None = None):

        super().__init__(tag, value, None, props)

    def to_html(self) -> str:

        if self.value is None:
            raise ValueError("No existing value")

        if self.tag is None:
            return self.value

        return (
            f"<{self.tag}{self.props_to_html()}>"
            f"{self.value}"
            f"</{self.tag}>"
        )

    def __repr__(self):
        return f"LeafNode (tag: {self.tag} | value: {
            self.value} | props: {self.props})"

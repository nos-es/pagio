from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            value: str,
            props: dict[str, str] | None = None):

        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:

        if self.value is None or self.value == "":
            raise ValueError("No existing value")

        if self.tag is None:
            return self.value

        props_html = super().props_to_html()

        html = f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

        return html

    def __repr__(self):
        print(f"LeafNode (tag: {self.tag} | value: {
              self.value} | props: {self.props})")

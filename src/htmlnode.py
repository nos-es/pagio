from __future__ import annotations


class HTMLNode:
    def __init__(
            self,
            tag: str | None = None,
            value: str | None = None,
            children: list[HTMLNode] | None = None,
            props: dict[str, str] | None = None):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:

        if self.props is None or self.props == {}:
            return ""

        props_str = ""
        for prop in self.props:
            props_str += f" {prop}=\"{self.props[prop]}\""

        return props_str

    def __repr__(self):
        print(f"HTMLNode (tag: {self.tag} | value: {self.value} | children: {
              self.children} | props: {self.props})")

from pagio.nodes.textnode import TextNode
from pagio.enums.texttype import TextType
from pagio.nodes.leafnode import LeafNode
from pagio.services.splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


def text_to_textnodes(text: str) -> list[TextNode]:
    text_node = TextNode(text, TextType.TEXT)
    result = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_image(result)
    result = split_nodes_link(result)

    return result


def text_node_to_html_node(text_node: TextNode) -> LeafNode:

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TextType.LINK:

        if text_node.url is None:
            raise ValueError("invalid url")

        return LeafNode("a", text_node.text, {"href": text_node.url})

    if text_node.text_type == TextType.IMAGE:

        if text_node.url is None:
            raise ValueError("invalid url")

        return LeafNode(
            "img", "", {"src": text_node.url, "alt": text_node.text})

    raise Exception("Type of this text node is not supprted")

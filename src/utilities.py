from textnode import TextNode, TextType
from leafnode import LeafNode


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
        return LeafNode("a", text_node.text, {"href": text_node.url})

    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            "img", "", {"src": text_node.url, "alt": text_node.text})

    raise Exception("Type of this text node is not supprted")


def has_closing_delimiter(text: str, delimiter: str) -> bool:

    if delimiter not in text:
        return False

    delimiter_count = 0

    for char in text:
        if char == delimiter:
            delimiter_count += 1

    return delimiter_count % 2 == 0


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    result_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue

        if not has_closing_delimiter(node.text, delimiter):
            raise Exception(
                "Provided delimiter does not exist in provided text or no closing delimiter in markdown.")

        splitted = node.text.split(delimiter)
        for i in range(0, len(splitted)):
            if splitted[i] == "":
                continue
            if i % 2 == 0:
                result_nodes.append(TextNode(splitted[i], TextType.TEXT))
            else:
                result_nodes.append(TextNode(splitted[i], text_type))

    return result_nodes

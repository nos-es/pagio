from textnode import TextNode, TextType
from leafnode import LeafNode
import re


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        if block == "":
            continue
        result.append(block.strip())

    return result


def text_to_textnode(text: str) -> list[TextNode]:
    text_node = TextNode(text, TextType.TEXT)
    result = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_image(result)
    result = split_nodes_link(result)

    return result


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue

        split_images = extract_markdown_images(node.text)
        node_text = node.text
        for image_pair in split_images:
            image_alt = image_pair[0]
            image_link = image_pair[1]
            split_string = f"![{image_alt}]({image_link})"

            sections = node_text.split(split_string, 1)
            result_nodes.append(TextNode(sections[0], TextType.TEXT))
            result_nodes.append(
                TextNode(image_alt, TextType.IMAGE, image_link))
            node_text = node_text[len(sections[0]) + len(split_string):]

        if node_text != "" and node_text is not None:
            result_nodes.append(TextNode(node_text, TextType.TEXT))

    return result_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue

        split_links = extract_markdown_links(node.text)
        node_text = node.text
        for link_pair in split_links:
            link_alt = link_pair[0]
            link_url = link_pair[1]
            split_string = f"[{link_alt}]({link_url})"

            sections = node_text.split(split_string, 1)
            result_nodes.append(TextNode(sections[0], TextType.TEXT))
            result_nodes.append(
                TextNode(link_alt, TextType.LINK, link_url))

            node_text = node_text[len(sections[0]) + len(split_string):]

        if node_text != "" and node_text is not None:
            result_nodes.append(TextNode(node_text, TextType.TEXT))

    return result_nodes


def extract_markdown_images(text: str) -> list[tuple(str, str)]:
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images


def extract_markdown_links(text: str) -> list[tuple(str, str)]:
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links


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

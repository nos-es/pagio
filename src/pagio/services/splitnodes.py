import re
from pagio.nodes.textnode import TextNode
from pagio.enums.texttype import TextType


def closing_delimiter_missing(splitted: list[str]) -> bool:

    return len(splitted) % 2 == 0


def extract_markdown_images(text: str) -> list[tuple(str, str)]:
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images


def extract_markdown_links(text: str) -> list[tuple(str, str)]:
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    result_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue

        split_nodes = []
        splitted = node.text.split(delimiter)

        if closing_delimiter_missing(splitted):
            raise Exception(
                "Provided delimiter has no closing delimiter in markdown.")

        for i in range(0, len(splitted)):
            if splitted[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(splitted[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(splitted[i], text_type))
        result_nodes.extend(split_nodes)

    return result_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue

        split_images = extract_markdown_images(node.text)
        if len(split_images) == 0:
            result_nodes.append(node)
            continue
        node_text = node.text
        for image_pair in split_images:
            image_alt = image_pair[0]
            image_link = image_pair[1]
            split_string = f"![{image_alt}]({image_link})"

            sections = node_text.split(split_string, 1)
            if len(sections) != 2:
                raise ValueError("Image in markdown has not closing sectio")
            if sections[0] != "":
                result_nodes.append(TextNode(sections[0], TextType.TEXT))

            result_nodes.append(
                TextNode(image_alt, TextType.IMAGE, image_link))

            node_text = sections[1]

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

        if len(split_links) == 0:
            result_nodes.append(node)
            continue

        node_text = node.text
        for link_pair in split_links:
            link_alt = link_pair[0]
            link_url = link_pair[1]
            split_string = f"[{link_alt}]({link_url})"

            sections = node_text.split(split_string, 1)

            if len(sections) != 2:
                raise ValueError("Link in markdown has not closing section")
            if sections[0] != "":
                result_nodes.append(TextNode(sections[0], TextType.TEXT))

            result_nodes.append(
                TextNode(link_alt, TextType.LINK, link_url))

            node_text = sections[1]

        if node_text != "" and node_text is not None:
            result_nodes.append(TextNode(node_text, TextType.TEXT))

    return result_nodes

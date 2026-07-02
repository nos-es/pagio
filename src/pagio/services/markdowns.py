import re
from pagio.nodes.parentnode import ParentNode
from pagio.nodes.htmlnode import HTMLNode
from pagio.enums.blocktype import BlockType
from pagio.services.blocktypes import block_to_blocktype
from pagio.services.texts import text_to_textnode


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        if block == "":
            continue
        result.append(block.strip())

    return result


def markdown_to_html_node(markdown_doc: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown_doc)
    root_children = []
    root_node = ParentNode("div", root_children)
    print(blocks)

    for block in blocks:
        print(f"Current Block: {block}")
        block_type = block_to_blocktype(block)
        text_nodes = text_to_textnode(block)
        print("text_nodes:")
        print(text_nodes)
        print("__________________________")
        # html_node = create_html_node_by_blocktype(block, block_type)

    return root_node


def create_html_node_by_blocktype(block: str, block_type: BlockType) -> HTMLNode:
    if block_type == BlockType.PARAGRAPH:
        return HTMLNode("p", block)
    pass

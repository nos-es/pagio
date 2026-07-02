import unittest
from textnode import TextNode, TextType
from blocktype import BlockType
from utilities import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, markdown_to_blocks, block_to_blocktype


class TestUtitilies(unittest.TestCase):

    def test_heading_level_1(self):
        block = "# This is a heading"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.HEADING)

    def test_heading_level_6(self):
        block = "###### This is a heading"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.HEADING)

    def test_seven_hashes_are_not_a_heading(self):
        block = "####### This is not a heading"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_hash_without_space_is_not_a_heading(self):
        block = "#Not a heading"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\nprint('hello')\n```"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.CODE)

    def test_unclosed_code_block_is_paragraph(self):
        block = "```\nprint('hello')"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_quote_block(self):
        block = "> First line\n> Second line"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- First item\n- Second item\n- Third item"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_ordered_list_must_start_at_one(self):
        block = "2. First item\n3. Second item"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_ordered_list_numbers_must_increment(self):
        block = "1. First item\n2. Second item\n4. Fourth item"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_ordered_list_requires_space_after_period(self):
        block = "1.First item\n2.Second item"

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_regular_text_is_paragraph(self):
        block = "This is a normal paragraph."

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_multiline_paragraph(self):
        block = "This is the first line.\nThis is the second line."

        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE,
                         "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(

            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_links_text_after_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev). Nothing more.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(

            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
                TextNode(". Nothing more.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.com)"
        )
        self.assertListEqual(
            [("link", "https://i.imgur.com/zjjcJKZ.com")], matches)

    def test_split_nodes_delimiter_not_text_type(self):
        text = "Hello `World`"
        delimiter = "`"

        text_node = TextNode(text, TextType.CODE)

        result_nodes = split_nodes_delimiter(
            [text_node], delimiter, TextType.CODE)

        expected_nodes = [
            TextNode("Hello `World`", TextType.CODE)]

        self.assertEqual(result_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_missing_closing_delimeter(self):
        text = "Hello _World"
        delimiter = "_"

        text_node = TextNode(text, TextType.TEXT)

        self.assertRaises(Exception, split_nodes_delimiter, [
                          text_node], delimiter, TextType.ITALIC)

    def test_bold_delimiter(self):
        text = "Hello **World**"
        delimiter = "**"

        text_node = TextNode(text, TextType.TEXT)

        result_nodes = split_nodes_delimiter(
            [text_node], delimiter, TextType.BOLD)

        expected_nodes = [
            TextNode("Hello ", TextType.TEXT), TextNode("World", TextType.BOLD)]

        self.assertEqual(result_nodes, expected_nodes)

    def test_italic_delimiter(self):
        text = "Hello _World_"
        delimiter = "_"

        text_node = TextNode(text, TextType.TEXT)

        result_nodes = split_nodes_delimiter(
            [text_node], delimiter, TextType.ITALIC)

        expected_nodes = [
            TextNode("Hello ", TextType.TEXT), TextNode("World", TextType.ITALIC)]

        self.assertEqual(result_nodes, expected_nodes)

    def test_code_delimiter(self):
        text = "Hello `World`"
        delimiter = "`"

        text_node = TextNode(text, TextType.TEXT)

        result_nodes = split_nodes_delimiter(
            [text_node], delimiter, TextType.CODE)

        expected_nodes = [
            TextNode("Hello ", TextType.TEXT), TextNode("World", TextType.CODE)]

        self.assertEqual(result_nodes, expected_nodes)

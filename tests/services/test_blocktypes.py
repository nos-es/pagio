import unittest
from pagio.services.blocktypes import block_to_blocktype
from pagio.enums.blocktype import BlockType


class TestBlockTypes(unittest.TestCase):

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

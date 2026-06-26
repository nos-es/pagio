import unittest
from textnode import TextNode, TextType
from utilities import split_nodes_delimiter


class TestUtitilies(unittest.TestCase):

    def test_split_nodes_delimiter_not_text_type(self):
        text = "Hello `World`"
        delimiter = "`"

        text_node = TextNode(text, TextType.CODE)

        result_nodes = split_nodes_delimiter(
            [text_node], delimiter, TextType.CODE)

        expected_nodes = [
            TextNode("Hello `World`", TextType.CODE)]

        print(f"Result Node: {result_nodes}")

        self.assertEqual(result_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_missing_delimeter(self):
        text = "Hello World"
        delimiter = "_"

        text_node = TextNode(text, TextType.TEXT)

        self.assertRaises(Exception, split_nodes_delimiter, [
                          text_node], delimiter, TextType.ITALIC)

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

import unittest
from textnode import TextNode, TextType
from utilities import split_nodes_delimiter


class TestUtitilies(unittest.TestCase):
    def test_bold_delimiter(self):
        text = "Hello **World**"
        delimiter = "**"

        text_node = TextNode(text, TextType.TEXT)

        result_nodes = split_nodes_delimiter(
            [text_node], delimiter, TextType.BOLD)

        expected_nodes = [
            TextNode("Hello ", TextType.TEXT), TextNode("World", TextType.BOLD)]

        self.assertEqual(result_nodes, expected_nodes)

import unittest
from textnode import TextNode, TextType
from utilities import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link


class TestUtitilies(unittest.TestCase):
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
        print(f"New nodes: {new_nodes}")
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

import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_returns_empty_string(self):
        test_node = HTMLNode()

        self.assertEqual(test_node.props_to_html(), "")

    def test_props_to_html_returns_props_string(self):
        props = {"href": "https://test.com", "for": "btn"}
        test_node = HTMLNode(props=props)

        self.assertEqual(test_node.props_to_html(),
                         " href=\"https://test.com\" for=\"btn\"")

    def test_props_to_html_returns_empty_string_when_props_is_none(self):
        props = None
        test_node = HTMLNode(props=props)

        self.assertEqual(test_node.props_to_html(), "")

import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_with_p(self):
        tag = "p"
        value = "This is a paragraph"
        test_leaf = LeafNode(tag, value)

        self.assertEqual(test_leaf.to_html(), f"<{tag}>{value}</{tag}>")

    def test_to_html_raise_value_error_when_value_none(self):
        tag = "a"
        value = None
        test_leaf = LeafNode(tag, value)

        self.assertRaises(ValueError, test_leaf.to_html)

    def test_to_html_raise_return_value_when_tag_none(self):
        tag = None
        value = "This is a test value"
        test_leaf = LeafNode(tag, value)

        self.assertEqual(test_leaf.to_html(), value)

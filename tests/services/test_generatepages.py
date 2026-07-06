import unittest
from pagio.services.generatepages import extract_title


class TestGeneratePages(unittest.TestCase):

    def test_extract_title_with_h1_heading(self):
        markdown = "# Hello"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello")

    def test_extract_title_with_beginning_whitespaces(self):
        markdown = "         # Hello"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello")

    def test_extract_title_with_new_lines_returns_title(self):
        markdown = "# Hello\n World"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello")

    def test_extract_title_with_missing_h1_heading_raises_exception(self):
        markdown = "Hello"
        self.assertRaises(Exception, extract_title, markdown)

    def test_extract_title_with_h2_heading_raises_exception(self):
        markdown = "## Hello"
        self.assertRaises(Exception, extract_title, markdown)

    def test_extract_title_with_multiple_hashtags_returns_title(self):
        markdown = "# I also code in C#"
        result = extract_title(markdown)
        self.assertEqual(result, "I also code in C#")

import unittest
from block_markdown import *

class TestBlockMarkdowns(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
# This is a heading

This is paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
            This is text          





This is another paragraph
This is in the same block

* This is a list
* This is another list
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is text",
                "This is another paragraph\nThis is in the same block",
                "* This is a list\n* This is another list",
            ],
        )


    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "> quote\nmore quote"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "* list\nitems"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "1. list\n3. items"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "2. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_extract_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), 'Hello')

if __name__ == "__main__":
    unittest.main()
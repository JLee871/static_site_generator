import unittest
from markdown_to_html import *

class Test_MD_to_HTML(unittest.TestCase):
    def test_text_to_children(self):
        text = 'This is a heading'
        self.assertListEqual(text_to_children(text), [HTMLNode(None, 'This is a heading', None, None)])
    
    def test_heading_to_html(self):
        block = '###### This is a heading'
        self.assertEqual(heading_to_html(block), ParentNode('h6', [LeafNode(None, 'This is a heading')]))
        
    def test_code_to_html(self):
        block = '```This is code```'
        self.assertEqual(code_to_html(block), ParentNode('pre', [LeafNode('code', 'This is code')]))

    def test_quote_to_html(self):
        block = '>This is a quote block\n>This is quote block'
        self.assertEqual(quote_to_html(block), ParentNode('blockquote', [LeafNode(None, 'This is a quote block\nThis is quote block')]))

    def test_ulist_to_html(self):
        block = '* list item 1\n* list item 2\n* list item 3'
        self.assertEqual(ulist_to_html(block), ParentNode('ul', [ParentNode('li', [LeafNode(None, 'list item 1')]), ParentNode('li', [LeafNode(None, 'list item 2')]),
                                                                 ParentNode('li', [LeafNode(None, 'list item 3')])]))

    def test_olist_to_html(self):
        block = '1. list item 1\n2. list item 2\n3. list item 3'
        self.assertEqual(olist_to_html(block), ParentNode('ol', [ParentNode('li', [LeafNode(None, 'list item 1')]), ParentNode('li', [LeafNode(None, 'list item 2')]),
                                                                 ParentNode('li', [LeafNode(None, 'list item 3')])]))        

    def test_markdown_to_html(self):
        md = """
### This is a heading

This is a paragraph of text.

* list item 1
* list item 2
* list item 3
"""
        self.assertEqual(markdown_to_html_node(md), ParentNode('div', [ParentNode('h3', [LeafNode(None, 'This is a heading')]), 
                                                                       ParentNode('p', [LeafNode(None, 'This is a paragraph of text.')]),
                                                                       ParentNode('ul', [ParentNode('li', [LeafNode(None, 'list item 1')]), ParentNode('li', [LeafNode(None, 'list item 2')]),
                                                                                         ParentNode('li', [LeafNode(None, 'list item 3')])])]))

if __name__ == "__main__":
    unittest.main()
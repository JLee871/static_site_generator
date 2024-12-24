import re
from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *
from markdown_to_html import *

def main():

    md = """
# This is a heading

This is paragraph of text.

* list item 1
* list item 2
* list item 3
"""
    list = (markdown_to_blocks(md))
    print(markdown_to_html_node(md))
        
    

if __name__ == "__main__":
    main()
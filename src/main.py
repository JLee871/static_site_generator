import re
from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *

def main():

    #text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
    #node = TextNode(text, TextType.NORMAL)
    #new_nodes = split_all([node])
    #print(text_to_textnodes(text))
    #print(split_nodes_link(new_nodes))
    #list = ['  a   ', 'b', 'c']
    #list[0] = list[0].lstrip().rstrip()
    #text = '# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item'
    #print(markdown_to_blocks(text))
    list = ['a']
    print(list[-1])
        
    

if __name__ == "__main__":
    main()
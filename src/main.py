import re
from textnode import *
from htmlnode import *
from split_delimiter import *

def main():

    text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
    node = TextNode(text, TextType.NORMAL)
    new_nodes = split_all([node])
    print(text_to_textnodes(text))
    #print(split_nodes_link(new_nodes))
        
    

if __name__ == "__main__":
    main()
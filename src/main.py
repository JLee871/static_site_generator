from textnode import *
from htmlnode import *
from split_delimiter import *

def main():
    node = ParentNode("p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(node.to_html())
    node = TextNode("This is text with a **bold** word", TextType.NORMAL)
    nodes = [TextNode("This is text with a **bold** word", TextType.NORMAL)]
    #print(split_bold(nodes))

    nodes2 = [TextNode("This is text with a **bold** word", TextType.NORMAL),
             TextNode("This is text with an *italic* word", TextType.NORMAL)]
    print(split_all(nodes2))
        
    

if __name__ == "__main__":
    main()
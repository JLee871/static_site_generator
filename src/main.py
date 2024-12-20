from textnode import *
from htmlnode import *

def main():
    node = HTMLNode("h1", "this is the text inside", None, {"href": "https://www.google.com", "target": "_blank"})
    print(node.props_to_html())
    


if __name__ == "__main__":
    main()
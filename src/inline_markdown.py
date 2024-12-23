import re
from textnode import TextType, TextNode

def split_nodes_delimiter(delimiter, text_type):
    def wrapper(old_nodes):
        new_nodes = []
        for node in old_nodes:
            new_nodes.extend(node_delimiter(node, delimiter, text_type))
        return new_nodes
    return wrapper

def node_delimiter(node, delimiter, text_type):
    new_nodes = []
    
    if node.text_type != TextType.NORMAL:
        return [node]

    text_split = node.text.split(delimiter, 2)
    if len(text_split) == 2:
        raise Exception('invalid markdown syntax. closing delimiter not found')
    if len(text_split) == 1:
        return [node]
    
    if text_split[0] != '':
        new_nodes.append(TextNode(text_split[0], TextType.NORMAL))
    new_nodes.append(TextNode(text_split[1], text_type))
    if text_split[2] != '':
        new_nodes.extend(node_delimiter(TextNode(text_split[2], TextType.NORMAL), delimiter, text_type))
    return new_nodes

split_bold = split_nodes_delimiter('**', TextType.BOLD)
split_italic = split_nodes_delimiter('*', TextType.ITALIC)
split_code = split_nodes_delimiter('`', TextType.CODE)

splits = [split_bold, split_italic, split_code]

def split_all(nodes):   
    new_nodes = nodes.copy()
    for item in splits:
        new_nodes = item(new_nodes)
    return new_nodes


def extract_markdown_images(text):
    alt_texts_urls = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_texts_urls

def extract_markdown_links(text):
    anchor_texts_urls = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return anchor_texts_urls

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        text = node.text
        if text == '':
            continue
        matches = extract_markdown_images(text)
        if matches == []:
            new_nodes.append(node)
            continue
        text_list = []
        for match in matches:
            alt_text, url = match
            text_list = text.split(f"![{alt_text}]({url})", 1)
            if text_list[0] != '':
                new_nodes.append(TextNode(text_list[0], TextType.NORMAL))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            text = text_list[1]
        if text != '':
            new_nodes.append(TextNode(text, TextType.NORMAL))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        text = node.text
        if text == '':
            continue
        matches = extract_markdown_links(text)
        if matches == []:
            new_nodes.append(node)
            continue        
        text_list = []
        for match in matches:
            alt_text, url = match
            text_list = text.split(f"[{alt_text}]({url})", 1)
            if text_list[0] != '':
                new_nodes.append(TextNode(text_list[0], TextType.NORMAL))
            new_nodes.append(TextNode(alt_text, TextType.LINKS, url))
            text = text_list[1]
        if text != '':
            new_nodes.append(TextNode(text, TextType.NORMAL))
    return new_nodes
               
def text_to_textnodes(text):
    node = TextNode(text, TextType.NORMAL)
    new_nodes = split_nodes_image(split_nodes_link(split_all([node])))
    return new_nodes

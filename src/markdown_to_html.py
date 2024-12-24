from htmlnode import *
from textnode import *
from inline_markdown import *
from block_markdown import *


def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children

def heading_to_html(block):
    heading_split = block.split(' ',1)
    heading_number = len(heading_split[0])
    return ParentNode(f'h{heading_number}', text_to_children(heading_split[1]))

def code_to_html(block):
    return ParentNode('pre', [ParentNode('code', text_to_children(block[4:-3]))])

def quote_to_html(block):
    if block[0:2] == '> ':
        lines = block.split('> ')
    else:
        lines = block.split('>')

    new_text = ''.join(lines)
    return ParentNode('blockquote', text_to_children(new_text))

def ulist_to_html(block):
    start = block[0:2]
    lines = block.split(start)
    list_items = []
    for line in lines[1:]:
        list_items.append(ParentNode('li', text_to_children(line.strip('\n'))))
    return ParentNode('ul', list_items)

def olist_to_html(block):
    lines = block.split('\n')
    list_items = []
    for line in lines:
        list_items.append(ParentNode('li', text_to_children(line[3:])))
    return ParentNode('ol', list_items)

def paragraph_to_html(block):
    return ParentNode('p', text_to_children(block))

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        match block_to_block_type(block):
            case 'heading':
                children.append(heading_to_html(block))
            case 'code':
                children.append(code_to_html(block))
            case 'quote':
                children.append(quote_to_html(block))
            case 'unordered list':
                children.append(ulist_to_html(block))
            case 'ordered list':
                children.append(olist_to_html(block))
            case 'paragraph':
                children.append(paragraph_to_html(block))
            case _:
                raise ValueError('invalid block type')
    return ParentNode('div', children)
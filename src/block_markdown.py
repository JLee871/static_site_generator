from enum import Enum

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    new_blocks = []
    for block in blocks:
        if not (block == '\n' or block == ''):
            new_blocks.append(block.strip())
    return new_blocks

def is_heading(block):
    return block.startswith(('#', '##', '###', '####', '#####', '######'))

def is_code(lines):
    if len(lines) < 2 and len(lines[0]) < 6:
        return False
    return (lines[0].startswith('```') and lines[-1].endswith('```'))

def is_quote(lines):
    for line in lines:
        if not line.startswith('>'):
            return False
    return True

def is_unordered_list(lines):
    start = ''
    if lines[0].startswith('* '):
        start = '* '
    elif lines[0].startswith('- '):
        start = '- '
    else:
        return False
    
    for line in lines:
        if not line.startswith(start):
            return False
    return True

def is_ordered_list(lines):
    i = 1
    for line in lines:
        str = f"{i}. "
        if not line.startswith(f"{i}. "):
            return False
        i += 1
    return True

def block_to_block_type(block):
    lines = block.split('\n')
    if is_heading(block):
        return block_type_heading
    if is_code(lines):
        return block_type_code
    if block.startswith('>'):
        if is_quote(lines):
            return block_type_quote
        return block_type_paragraph
    if block.startswith(('* ', '- ')):
        if is_unordered_list(lines):
            return block_type_ulist
        return block_type_paragraph
    if block.startswith('1. '):
        if is_ordered_list(lines):
            return block_type_olist
        return block_type_paragraph
    return block_type_paragraph

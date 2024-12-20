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

split_set = {split_bold, split_italic, split_code}

def split_all(nodes):
    new_nodes = nodes.copy()
    for item in split_set:
        new_nodes = item(new_nodes)
    return new_nodes
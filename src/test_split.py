import unittest

from split_delimiter import *


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        nodes = [TextNode("This is text with a **bold** word", TextType.NORMAL)]
        self.assertEqual(split_bold(nodes), [TextNode('This is text with a ', TextType.NORMAL, None), 
                                             TextNode('bold', TextType.BOLD, None), 
                                             TextNode(' word', TextType.NORMAL, None)])

    def test_italic(self):
        nodes = [TextNode("This is text with an *italic* word", TextType.NORMAL)]
        self.assertEqual(split_italic(nodes), [TextNode('This is text with an ', TextType.NORMAL, None), 
                                               TextNode('italic', TextType.ITALIC, None), 
                                               TextNode(' word', TextType.NORMAL, None)])
        
    def test_code(self):
        nodes = [TextNode("This is text with a `code` word", TextType.NORMAL)]
        self.assertEqual(split_code(nodes), [TextNode('This is text with a ', TextType.NORMAL, None), 
                                             TextNode('code', TextType.CODE, None), 
                                             TextNode(' word', TextType.NORMAL, None)])

    def test_multiple_bold(self):
        nodes = [TextNode("This is text with a **bold** word and **these words are bold too**", TextType.NORMAL)]
        self.assertEqual(split_bold(nodes), [TextNode('This is text with a ', TextType.NORMAL, None), 
                                             TextNode('bold', TextType.BOLD, None), 
                                             TextNode(' word and ', TextType.NORMAL, None),
                                             TextNode('these words are bold too', TextType.BOLD, None)])
    
    def test_multiple_types(self):
        nodes = [TextNode("This is text with a **bold** and *italic* and `code` words", TextType.NORMAL)]
        self.assertEqual(split_code(split_italic(split_bold(nodes))), [TextNode('This is text with a ', TextType.NORMAL, None), 
                                                                       TextNode('bold', TextType.BOLD, None), 
                                                                       TextNode(' and ', TextType.NORMAL, None),
                                                                       TextNode('italic', TextType.ITALIC, None),
                                                                       TextNode(' and ', TextType.NORMAL, None),
                                                                       TextNode('code', TextType.CODE, None),
                                                                       TextNode(' words', TextType.NORMAL, None)])

    def test_multiple_nodes(self):
        nodes = [TextNode("This is text with a **bold** word", TextType.NORMAL),
                 TextNode("This is text with an *italic* word", TextType.NORMAL)]
        new_nodes = split_all(nodes)
        print(new_nodes)
        self.assertEqual(new_nodes, [TextNode('This is text with a ', TextType.NORMAL, None), 
                                                                       TextNode('bold', TextType.BOLD, None), 
                                                                       TextNode(' word', TextType.NORMAL, None),
                                                                       TextNode('This is text with an ', TextType.NORMAL, None), 
                                                                       TextNode('italic', TextType.ITALIC, None), 
                                                                       TextNode(' word', TextType.NORMAL, None)])
    
    def test_empty(self):
        nodes = []
        self.assertEqual(split_code(split_italic(split_bold(nodes))), [])

    def test_entire_text_is_delimited(self):
        nodes = [TextNode("**This entire text is bold**", TextType.NORMAL)]
        self.assertEqual(split_bold(nodes), [TextNode('This entire text is bold', TextType.BOLD)])
        

if __name__ == "__main__":
    unittest.main()
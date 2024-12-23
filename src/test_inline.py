import unittest

from inline_markdown import *


class TestInlineMarkdowns(unittest.TestCase):
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
        self.assertEqual(split_all(nodes), [TextNode('This is text with a ', TextType.NORMAL, None), 
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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://google.com)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://google.com"),
            ],
            matches,
        )

    def test_split_nodes_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(text, TextType.NORMAL)
        node2 = node
        self.assertListEqual([TextNode('This is text with a link ', TextType.NORMAL, None), 
                              TextNode('to boot dev', TextType.LINKS, 'https://www.boot.dev'),
                              TextNode(' and ', TextType.NORMAL, None),
                              TextNode('to youtube', TextType.LINKS, 'https://www.youtube.com/@bootdotdev'),
                              TextNode('This is text with a link ', TextType.NORMAL, None),
                              TextNode('to boot dev', TextType.LINKS, 'https://www.boot.dev'),
                              TextNode(' and ', TextType.NORMAL, None), 
                              TextNode('to youtube', TextType.LINKS, 'https://www.youtube.com/@bootdotdev')],
                              split_nodes_link([node, node2]))
    
    def test_split_nodes_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        node = TextNode(text, TextType.NORMAL)
        self.assertListEqual([TextNode('This is text with a ', TextType.NORMAL, None),
                              TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'),
                              TextNode(' and ', TextType.NORMAL, None),
                              TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg')],
                              split_nodes_image([node]))
        
    def test_split_nodes_image_empty(self):
        self.assertListEqual([], split_nodes_image([]))

    def test_split_nodes_image_empty2(self):
        node = TextNode('', TextType.NORMAL)
        self.assertListEqual([], split_nodes_image([node, node, node]))

    def test_text_to_textnodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        self.assertListEqual([TextNode("This is ", TextType.NORMAL),
                              TextNode("text", TextType.BOLD),
                              TextNode(" with an ", TextType.NORMAL),
                              TextNode("italic", TextType.ITALIC),
                              TextNode(" word and a ", TextType.NORMAL),
                              TextNode("code block", TextType.CODE),
                              TextNode(" and an ", TextType.NORMAL),
                              TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                              TextNode(" and a ", TextType.NORMAL),
                              TextNode("link", TextType.LINKS, "https://boot.dev"),],
                              text_to_textnodes(text))

if __name__ == "__main__":
    unittest.main()
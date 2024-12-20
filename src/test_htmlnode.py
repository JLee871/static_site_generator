import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class Test_HTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode()
        output = "HTMLNode(None, None, None, None)"
        self.assertEqual(repr(node), output)

    def test_repr2(self):
        node = HTMLNode("h1", "this is the text inside")
        output2 = "HTMLNode(h1, this is the text inside, None, None)"
        self.assertEqual(repr(node), output2)

    def test_props_to_html(self):
        node = HTMLNode("h1", "this is the text inside", None, {"href": "https://www.google.com", "target": "_blank"})
        output2 = " href='https://www.google.com' target='_blank'"
        self.assertEqual(node.props_to_html(), output2)
    
    def test_leafnode_to_html(self):
        node = LeafNode("p", "this is the text", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<p href='https://www.google.com'>this is the text</p>")

    def test_leafnode_to_html_no_tag(self):
        node = LeafNode(None, "this is the text")
        self.assertEqual(node.to_html(), "this is the text")

    def test_parentnode_to_html(self):
        node = ParentNode("p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parentnode_to_html_nested(self):
        node = ParentNode("p",
                [
                    ParentNode("b", [
                        LeafNode("i", "Bold and italic text"),
                        LeafNode(None, "bold text")
                        ]
                    ),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
        self.assertEqual(node.to_html(), "<p><b><i>Bold and italic text</i>bold text</b><i>italic text</i>Normal text</p>")

    def test_parentnode_to_html_empty_child(self):
        node = ParentNode("p",
                [
                    ParentNode("b", [
                        LeafNode("i", "Bold and italic text"),
                        LeafNode(None, "bold text")
                        ]
                    ),
                    ParentNode("i", []),
                ],
            )
        self.assertEqual(node.to_html(), "<p><b><i>Bold and italic text</i>bold text</b><i></i></p>")

    

    
if __name__ == "__main__":
    unittest.main()
import unittest

from htmlnode import HTMLNode


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
        output2 = "href='https://www.google.com' target='_blank'"
        self.assertEqual(node.props_to_html(), output2)

    
if __name__ == "__main__":
    unittest.main()
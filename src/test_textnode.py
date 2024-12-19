import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.ITALIC, None)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
        self.assertTrue(node == node2)

    def test_noteq(self):
        node = TextNode("test", TextType.ITALIC, None)
        node2 = TextNode("test", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_err(self):
        with self.assertRaises(AttributeError):
            print(TextNode("test", 17))


if __name__ == "__main__":
    unittest.main()
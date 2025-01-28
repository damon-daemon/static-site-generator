import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_with_values(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_edge_case(self):
        node = HTMLNode(props={"class": "button-primary", "data-id": "12345"})
        self.assertEqual(node.props_to_html(), ' class="button-primary" data-id="12345"')

    def test_props_empty_attribute_values(self):
        node = HTMLNode(props={"disabled": "", "checked": ""})
        self.assertEqual(node.props_to_html(), ' disabled="" checked=""')


class TestLeafNode(unittest.TestCase):
    
    # Test case 1: If there's no value
    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    # Test case 2: If there's no tag
    def test_no_tag(self):
        node = LeafNode(None, "hello")
        result = node.to_html()
        self.assertEqual(result, "hello")

    # Test case 3: Simple tag with value
    def test_simple_tag_with_value(self):
        node = LeafNode("p", "hello")
        result = node.to_html()
        self.assertEqual(result, "<p>hello</p>")

    # Test case 4: Tag with props
    def test_tag_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()
        self.assertEqual(result, '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()


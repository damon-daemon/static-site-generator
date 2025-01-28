import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()


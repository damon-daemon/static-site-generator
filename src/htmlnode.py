class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_list = []
        if not self.props:
            return ""
        for key, value in self.props.items():
            props_list.append(f'{key}="{value}"')
        final_props = " ".join(props_list)
        return f" {final_props}"

class LeafNode(HTMLNode):
    def __init__(self, ):

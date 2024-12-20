class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        output = ""
        if self.props == None:
            return output
        for prop in self.props:
            if not output:
                output = f"{prop}='{self.props[prop]}'"
            else:
                output += f" {prop}='{self.props[prop]}'"
        return output

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        

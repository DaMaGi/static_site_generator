class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError("to_html method must be implemented by subclasses")
    
    def props_to_html(self):
        return "".join(f" {k}=\"{v}\"" for k, v in self.props.items())
    
    def __repr__(self):
        return f"Tag: {self.tag}, \nValue: {self.value}, \nChildren: {[c.tag for c in self.children]}, \nProperties: {self.props_to_html()}"
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
        return f"Tag: {self.tag}, \nValue: {self.value}, \nChildren: {[c.tag for c in self.children]}, \nProperties:{self.props_to_html()}"
        return f"Tag: {self.tag}, \nValue: {self.value}, \nChildren: {[c.tag for c in self.children]}, \nProperties:{self.props_to_html()}"


class LeafNode(HtmlNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"Tag: {self.tag}, \nValue: {self.value}, \nProperties: {self.props_to_html()}"
        return f"Tag: {self.tag}, \nValue: {self.value}, \nProperties: {self.props_to_html()}"

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value property.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag property.")
        if self.children is None:
            raise ValueError("ParentNode must have a children property.")
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

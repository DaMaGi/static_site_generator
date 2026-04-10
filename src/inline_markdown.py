# import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


# TODO: Include better pattern recognitions for each style and add single '*' to italics. Styles should have a /w character next to them.
# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []
#     for old_node in old_nodes:
#         if old_node.text_type != TextType.TEXT:
#             new_nodes.append(old_node)
#             continue
#         active_styles = {TextType.BOLD: False, TextType.ITALIC: False, TextType.CODE: False}
#         split_nodes = []
#         sections = re.split(r"**|_|`", old_node.text)
#         for sect in sections:
#             if sect == "":
#                 continue
#             match sect:
#                 case '**':
#                     active_styles ^= {TextType.BOLD}
#                 case '_':
#                     active_styles ^= {TextType.ITALIC}
#                 case '`':
#                     active_styles ^= {TextType.CODE}
#                 case _:
#                     split_nodes.append(TextNode(sect, {k for k, v in active_styles if v is True}))
#         new_nodes.extend(split_nodes)
#     return new_nodes

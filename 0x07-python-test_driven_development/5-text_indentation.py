#!/usr/bin/python3
"""adds indentations to input text"""


def text_indentation(text):
    """adds indentations to input text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    print("\n".join([line.strip() for line in text.split("\n")]), end="")

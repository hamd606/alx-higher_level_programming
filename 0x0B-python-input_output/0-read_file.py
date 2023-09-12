#!/usr/bin/python3
"""this module has function that do stuff
I believe that the dowcs will just waste your time it"s very simple"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read(), end="")

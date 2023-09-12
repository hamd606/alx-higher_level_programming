#!/usr/bin/python3
"""a module that tests the jsmon module"""


import json


def from_json_string(my_str):
    """writes an Object to a text file, using a JSON representation"""
    return json.loads(my_str)

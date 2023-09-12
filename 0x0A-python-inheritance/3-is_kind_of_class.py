#!/usr/bin/python3
"""This module has a funcction that check if a class is instance"""


def is_same_class(obj, a_class):
    """this function check if obj is an instannce of a a_class
    obj: an object
    a_class: a class
    Returns: Bool"""
    return isinstance(obj, a_class)

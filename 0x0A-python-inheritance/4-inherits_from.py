#!/usr/bin/python3
"""This module has a funcction that check if a class is instance"""


def is_same_class(obj, a_class):
    """his function check if obj is an istannce of a a_class"""
    if type(obj) is a_class:
        return Fasle
    else:
        return isinstance(obj, a_class)

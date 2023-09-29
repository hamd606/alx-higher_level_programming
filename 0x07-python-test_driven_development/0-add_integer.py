#!/usr/bin/python3
"""
This is an exercise  module.

The module supplies one function, add_integer().  For example,

add_integer(5, 6)
11
"""


def add_integer(a, b=98):
    """Return the sum of a and b, an integers or floats
    (casted to integers iside the function)"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)

    return a + b

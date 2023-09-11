#!/usr/bin/python3
"""this is a class inheritance f-rom list class"""


class MyList(list):
    """class that extends the list class"""
    def print_sorted(self):
        """a function that prints a sorted list"""
        print(sorted(self))

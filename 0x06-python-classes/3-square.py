#!/usr/bin/python3
"""This is a clas that representss a square """


class Square():
    """square class"""
    def __init__(self, size=0):
        """class init"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self._size ** 2

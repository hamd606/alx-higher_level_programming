#!/usr/bin/python3
"""This module implements a rectangle class"""


class Rectangle():
    """this is a rectangle class"""
    def __init__(self, width=0, height=0):
        """the init method"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """this is the width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """this is the height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area retriever"""
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.height * 2

    def __str__(self):
        graphical_rec = ""
        if self.__height == 0 or self.__width == 0:
            return graphical_rec
        for i in range(self.__height):
            for j in range(self.__width):
                graphical_rec += "#"
            graphical_rec += "\n"
        return graphical_rec[:len(graphical_rec) - 1]

#!/usr/bin/python3
"""This module implements a rectangle class"""


class Rectangle():
    """this is a rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """the init method"""
        self.__width = width
        self.__height = height
        #self.print_symbol = self.__class__.print_symbol
        self.__class__.number_of_instances += 1

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
                graphical_rec += str(self.print_symbol)
            graphical_rec += "\n"
        return graphical_rec[:len(graphical_rec) - 1]

    def __repr__(self):
        w = self.__width
        h = self.__height
        return "Rectangle(" + str(w) + ", " + str(h) + ")"

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

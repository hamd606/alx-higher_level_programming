#!/usr/bin/python3
"""This module has a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """this class is the rectangle class"""

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """class init method"""
        super().__init__(id)
        self.validate_int("width", width, possible_zero=False)
        self.validate_int("height", height, possible_zero=False)
        self.validate_int("x", x)
        self.validate_int("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.validate_int("width", value, possible_zero=False)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.validate_int("height", value, possible_zero=False)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y getter"""
        self.validate_int("y", value)
        self.__x = value
        self.__y = value

    @staticmethod
    def validate_int(var, value, possible_zero=True):
        """int validator"""
        if type(value) != int:
            raise TypeError(var + " must be an integer")
        if possible_zero and value < 0:
            raise ValueError(var + " must be >= 0")
        if not possible_zero and value < 1:
            raise ValueError(var + " must be > 0")

        return value

    def area(self):
        """area getter"""
        return self.__width * self.__height

    def display(self):
        """displays a rectangle"""
        print("\n"*self.__y, end="")
        for i in range(self.__height):
            print(" "*self.__x, end="")
            for j in range(self.__width):
                print("#", end="")

            print()

    def __str__(self):
        """str formatting"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update_helper(self, id=None, width=None, height=None, x=None, y=None):
        """updates attrib (helper func for update func"""
        if id is not None:
            self.id = id
        if width is not None:
            self.__width = width
        if height is not None:
            self.__height = height
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

    def update(self, *args, **kwargs):
        """updates attrib"""
        if args:
            self.update_helper(*args)
        if kwargs:
            self.update_helper(**kwargs)

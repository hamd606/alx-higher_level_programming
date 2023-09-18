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
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_int("height", value, possible_zero=False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        self.__x = value
        self.__y = value

    @staticmethod
    def validate_int(var, value, possible_zero=True):
        if type(value) != int:
            raise TypeError(var + " must be an integer")
        if possible_zero and value < 0:
            raise ValueError(var + " must be >= 0")
        if not possible_zero and value < 1:
            raise ValueError(var + " must be > 0")
        
        return value
    
    def area(self):
        return self.__width * self.__height
    
    def display(self):
        print("\n"*self.__y, end="")
        for i in range(self.__height):
            print(" "*self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
    def update_helper(self, id=None, width=None, height=None, x=None, y=None):
        if id != None:
            self.id = id
        if width != None:
            self.__width = width
        if height != None:
            self.__height = height
        if x != None:
            self.__x = x
        if y != None:
            self.__y = y

    def update(self, *args, **kwargs):
        if args:
            self.update_helper(*args)
        if kwargs:
            self.update_helper(**kwargs)

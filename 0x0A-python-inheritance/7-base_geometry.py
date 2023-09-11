#!/usr/bin/python3
"""empty class named geo..."""


class BaseGeometry():
    """empty class"""

    @classmethod
    def area(self):
        """calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if a num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

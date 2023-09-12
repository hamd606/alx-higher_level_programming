#!/usr/bin/python3
"""class for student creation"""


class Student:
    """Student obj class"""

    def __init__(self, first_name, last_name, age):
        """obj initiation method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """export method"""
        return self.__dict__

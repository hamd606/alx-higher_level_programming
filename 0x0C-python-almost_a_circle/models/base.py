#!/usr/bin/python3
"""This module has the base class
that all other classes inherits f-rom"""


class Base():
    """this class is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class init method"""
        if id != None:
            self.id = id

        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @classmethod
    def current_nb_obj(cls):
        return int(cls.__nb_objects)

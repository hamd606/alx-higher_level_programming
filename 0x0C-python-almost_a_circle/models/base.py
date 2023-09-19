#!/usr/bin/python3
"""This module has the base class
that all other classes inherits f-rom"""
from json import dumps, loads
import csv


class Base():
    """this class is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class init method"""
        if id is not None:
            self.id = id

        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @classmethod
    def current_nb_obj(cls):
        return int(cls.__nb_objects)

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open(f"{cls.__class__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """from json to dict"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance from dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new_obj = Rectangle(2, 2)
        elif cls is Square:
            new_obj = Square(2)
        else:
            new = None
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """loads from file"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

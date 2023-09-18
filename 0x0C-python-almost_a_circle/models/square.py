#!/usr/bin/python3
"""this module has a square class (based on Rectangle)"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this is a square!"""
    def __init__(self, size=0, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
    
    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.validate_int("width", value, possible_zero=False)
        self.validate_int("height", value, possible_zero=False)
        self.width = value
        self.height = value
        
    def update_helper(self, id=None, size=None, x=None, y=None):
        '''updates method for args'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates attributes via *args and **kargs'''
        if args:
            self.update_helper(*args)
        elif kwargs:
            self.update_helper(**kwargs)

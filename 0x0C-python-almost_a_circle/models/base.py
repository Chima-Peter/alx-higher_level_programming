#!usr/bin/python3
"""
Module that creates the first class Base
"""


class Base:
    """
    Class Base with:
        private class attribute __nb_objects
        class constructor __init
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Class contructor for Base, increments __nb_objects and set\
                value to id
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

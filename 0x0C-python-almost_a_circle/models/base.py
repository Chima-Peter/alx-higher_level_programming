#!usr/bin/python3
"""
Module that creates the first class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dict):
        """
        returns the JSON string representation of list_dictionaries:
        """
        if type(list_dict) == None or len(list_dict) == 0:
                return "[]"
        return json.dumps(list_dict)

    @classmethid
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        name = cls.__class__.__nam__ + ".json"
        with open(name, "w+", encoding="UTF-8"):
            if type(list_objs) == None:
                write(" ")
            write(to_json_string(list_objs))

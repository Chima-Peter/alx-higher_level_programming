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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        """
        returns the JSON string representation of list_dictionaries:
        """
        if type(list_dict) is None or len(list_dict) is 0:
            return "[]"
        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        name = cls.__name__ + ".json"
        with open(name, "w+", encoding="UTF-8") as f:
            if type(list_objs) is None:
                f.write(" ")
            new_list = []
            for i in range(len(list_objs)):
                new_list.append(cls.to_dictionary(list_objs[i]))
            f.write(json.dumps(new_list))

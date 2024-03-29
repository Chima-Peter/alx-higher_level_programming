#!/usr/bin/python3
"""
Module that creates the first class Base
"""
import json
import os.path


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
        if type(list_dict) is None or len(list_dict) == 0:
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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        """
        new_list = []
        if type(json_string) is None:
            return new_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            r1 = cls(1, 1, 1, 1, 0)
            r1.update(**dictionary)
            return str(r1)

        elif cls.__name__ == "Square":
            s1 = cls(1, 1, 1, 0)
            s1.update(**dictionary)
            return str(s1)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        new_list = []
        name = cls.__name__ + ".json"

        if os.path.exists(name) is False:
            return new_list

        with open(name, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for row in lines:
                old_dict = cls.from_json_string(row)
        for row in old_dict:
            new_list.append(cls.create(**row))
        return new_list

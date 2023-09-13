#!/usr/bin/python3
"""
Module that creates a class Student
"""


class Student:
    """
    A class Student that defines a student by:
    Args:
        Public instance attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialisation of class with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=[]):
        """
        Retrieves a dictionary representaion of a Student instance
        """
        new_dict = {'first_name': self.first_name}
        new_dict['last_name'] = self.last_name
        new_dict['age'] = self.age
        if len(attrs) == 0:
            return new_dict
        fake_dict = {}
        for name in attrs:
            for key in new_dict:
                if name == key:
                    fake_dict[key] = new_dict[key]
        return fake_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']

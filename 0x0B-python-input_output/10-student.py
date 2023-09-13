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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representaion of a Student instance
        """
        new_dict = {'first_name': self.first_name}
        new_dict['last_name'] = self.last_name
        new_dict['age'] = self.age
        for key in new_dict:
            if key not in attrs:
                del new_dict[key]
        return new_dict

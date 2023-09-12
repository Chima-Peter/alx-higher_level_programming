#!/usr/bin/python3
"""
Module that creates the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Function that checks if obj is an instance of or if obj is a\
            subclass of the specified class
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False

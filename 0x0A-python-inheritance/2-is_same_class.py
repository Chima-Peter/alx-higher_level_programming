#!/usr/bin/python3
"""
Module that creates the is_same_class function
"""


def is_same_class(obj, a_class):
    """
    function that checks if object is exactly an instance of class
    """
    if type(obj) == a_class:
        return True
    else:
        return False

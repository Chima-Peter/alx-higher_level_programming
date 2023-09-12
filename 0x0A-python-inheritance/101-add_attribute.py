#!/usr/bin/python3
"""
Module that creates the add_attribute function
"""


def add_attribute(obj, name, value):
    """
    Tries to add a new attribute to an object if possible
    """
    setattr(obj, name, value)
    if hasattr(obj, name) is False:
        raise TypeError("can't add new attribute")

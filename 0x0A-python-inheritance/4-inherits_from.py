#!/usr/bin/python3
"""
Module that creates the inheirts_from function
"""


def inherits_from(obj, a_class):
    """
    Function that checks for subclass
    """
    if issubclass(obj, a_class) == True:
        return True
    else:
        return False

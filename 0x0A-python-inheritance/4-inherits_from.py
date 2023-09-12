#!/usr/bin/python3
"""
Module that creates the inheirts_from function
"""


def inherits_from(obj, a_class):
    """
    Function that checks for subclass
    """
    if isinstance(obj, a_class) is True and type(obj) is not a_class:
        return True
    else:
        return False

#!/usr/bin/python3
"""
Creates a function for addition
Prototype def add_integer(a, b=98)
No importaion of modules
"""


def add_integer(a, b=98):
    """
    Function that validates, then adds two integers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    a = int(a)
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    b = int(b)
    return a + b

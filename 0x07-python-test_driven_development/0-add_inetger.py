#!/usr/bin/python3
"""
Creates a function for addition
"""
def add_integer(a, b=98):
    if type(a) != int or type(a) != float:
        raise TyoeError("a must be an integer")
    a = int(a)
    if type(b) != int or type(b) != float:
        raise TyoeError("b must be an integer")
    b = int(b)
    return a + b

#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(arg=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(arg) == 0:
        return None
    if type(arg) != list:
        raise TypeError("can only pass list as argument")
    result = arg[0]
    i = 1
    while i < len(arg):
        if type(arg[i]) != int:
            raise TypeError("llist can only contain integers")
        if arg[i] > result:
            result = arg[i]
        i += 1
    return result

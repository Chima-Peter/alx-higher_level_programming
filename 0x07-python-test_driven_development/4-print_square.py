#!/usr/bin/python3
"""
Write a function that prints a square with the character #.
Prototype: def print_square(size):
"""


def print_square(size):
    """
    Prints a square usin the character # size number of times
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size == 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for n in range(size):
            print("#".end="")
        print()

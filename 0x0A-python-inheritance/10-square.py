#!/usr/bin/python3
"""
Module that inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that inherits Rectangle from 9-rectangle
    """
    def __init__(self, size):
        """
        Initialises the class witn size
        """
        super().__init__(size, size)
        self.__size = size

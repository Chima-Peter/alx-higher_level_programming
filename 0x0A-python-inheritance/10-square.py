#!/usr/bin/python3
"""
Module that inherits from Rectangle (9-rectangle.py)
"""


class Square(Rectangle):
    """
    Class that inherits Rectangle from 9-rectangle
    """
    def __init__(self, size):
        super().__init__(size, size)
        """
        Initialises the class witn size
        """
        """
        super().integer_validator(self, 'size', size)
        self.__size = size
        
    def area(self):
        """
#        Calculates the area of a square
        """
        return self.__size * self.__size"""

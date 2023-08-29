#!/usr/bin/python3
"""Creates a class Square that's based on 3-square.py"""


class Square:
    """Defines a class that's initialised with a private attribute"""

    def __init__(self, size=0):
        """Initialises attributes for the Square class. It validates
        size argument by checking TypeError and ValueError
    Args:
        size: the size of the square and set to 0 by default
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieves the value of size
            Return: the value of size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of size
        Args:
                value: the new value of size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a square using it's size
            Return: the area
        """
        return self.__size ** 2

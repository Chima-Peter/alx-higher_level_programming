#!/usr/bin/python3
"""
Creates a class Rectangle that defines a a rectangle
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle with:
    Instantiation with optional width and height using __init__
    """
    def __init__(self, width=0, height=0):
        """
        Initialises the class with certain attributes.
        Args:
            height and also validates it
            width and also validates it too
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        """
        Method to retrieve the value of width.

        Return: The value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Method to set and validate value new value of width.
        Args:
            Value: the new value to be assigned
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Method to retrieve the value of height.

        Return: The value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Method to set and validate value new value of height.
        Args:
            Value: the new value to be assigned
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

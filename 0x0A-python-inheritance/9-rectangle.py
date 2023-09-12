#!/usr/bin/python3
"""
Module that creates the class Rectangle based on 8-base_geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initailises the class with width and height\
                validated by integer_validator
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Printing to output once function is called with print or str
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

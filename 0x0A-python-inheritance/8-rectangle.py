#!/usr/bin/python3
"""
Module that creates the class Rectangle
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

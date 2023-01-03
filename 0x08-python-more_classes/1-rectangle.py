#!/usr/bin/python3
"This module creates a class that defines 2 private instance attributes"
class Rectangle:
    "This classs creates 2 private attribues "
    def __init__(self, width, height):
        "This function initialises the attributes"
        self.width = width
        self.height = height
    @property
    def width(self):
        "Gets the new value of width"
        return self.__width
    @width.setter
    def width(self, value):
        "Sets the new value of width"
        if type(value) != int:
            "Checks if value is an integer"
            raise TypeError("width must be an integer")
        elif value < 0:
            "Checks if value if less than 0"
            raise ValueError("width must be >= 0")
        else:
            "Sets the new value of width if all checks were passed"
            self.__width = value
    @property
    def height(self):
        "This function gets the new value of heihght"
        return self.__height
    @height.setter
    def height(self, value):
        "This function sets the new value for height"
        if type(value) != int:
            "Checks if value if of type int"
            raise TypeError("height must be an integer")
        elif value < 0:
            "Checks if value is > 0"
            raise ValueError("height must be >= 0")
        else:
            "Sets value if all checks were met"
            self.__height = value

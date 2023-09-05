#!/usr/bin/python3
"""
Creates a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle with:
        Args:
            Instantiation with optional width and height using init
            Public instance method: def area(self)
            Public instance method: def perimeter(self)
            Magic method __str__
            Magic method __repr__
            Magic method __del__
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

    def area(self):
        """
        Method to calculate area of rectangle using the formula

        Return: the caluculated area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method to calculate perimeter of rectangle using the formula

        Return: the caluculated perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Method to print a rectangle with character #;should work same
        as calling print function
        Return: the rectangle or empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range(self.__height):
            for n in range(self.__width):
                print("#", end="")
            if i < (self.__height - 1):
                print()
        return ''

    def __repr__(self):
        """
        Method to return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...)

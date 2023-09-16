#!/usr/bin/python3
"""
Module for writing a class Rectangle that inherits from class Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inheirts from Base
    Args:
        Private instance attributes, each having getter and setter
        Class constructor __init__
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor that:
            Call the super class with id
            Assign each argument to their right attributes
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        width getter
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        Width Setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must > 0")
        self.__width = width

    @property
    def height(self):
        """
        Height getter
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        Height setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        X getter
        """
        return self.__x
    @x.setter
    def x(self, value):
        """
        X setter
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueErro("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Y getter
        """
        return self.__y
    @y.setter
    def y(self, value):
        """
        Y setter
        """
        if type(value)!= int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

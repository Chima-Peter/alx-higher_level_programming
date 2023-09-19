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

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must > 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        self.__width = value

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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

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
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method to calculate the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Method that returns to stdout
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """
        print in stdout the Rectangle instance with the character # by taking care of x and y
        """

        for i in range(self.__height):
            for x in range(max(self.__x, self.__y)):
                print(" ", end="")
            for n in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Assigns each argument to each attribute
        """
        my_list = [self.id, self.__width, self.__height, self.__x, self.__y]
        for i in range(len(args)):
            my_list[i] = args[i]
        self.id = my_list[0]
        self.__width = my_list[1]
        self.__height = my_list[2]
        self.__x = my_list[3]
        self.__y = my_list[4]

        if len(args) == 0:
            my_dict = {'id': self.id, 'width': self.__width, 'height': self.__height, 'x': self.__x, 'y': self.__y}
            for key in kwargs:
                my_dict[key] = kwargs[key]
            self.id = my_dict['id']
            self.__width = my_dict['width']
            self.__height = my_dict['height']
            self.__x = my_dict['x']
            self.__y = my_dict['y']

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        new_dict = {'id': self.id, 'width': self.__width, 'height': self.__height, 'x': self.__x, 'y': self.__y}
        return new_dict

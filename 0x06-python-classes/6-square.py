#!/usr/bin/python3
"""Creates a class Square that's based on 5-square.py"""


class Square:
    """Defines a class that's initialised with a private attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialises attributes for the Square class. It validates
        the argument by checking TypeError and ValueError
    Args:
        size: the size of the square and set to 0 by default
        position: a tuple that holds the coordinates of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the values of position
            Return: the new coordinates
        """
        return self.__position

    @position.setter
    def postion(self, value):
        """Sets the new coordinates
            Args:
                Value: the new coordinates
        """
        if type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__value = value

    def area(self):
        """Calculates the area of a square using it's size
            Return: the area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__position[0] > self.__position[1]:
            mark = self.__position[0]
        else:
            mark = self.__position[1]
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(mark):
                    print(" ", end="")
                for n in range(self.__size):
                    print("#", end="")
                print()

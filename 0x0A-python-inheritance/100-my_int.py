#!/usr/bin/python3
"""
Module that creates the MyInt class
"""


class MyInt:
    """
    Implements the inversion of the == and =! operators
    """
    def __init__(self, num):
        """
        Initialises the class with num
        """
        self.__num = num


    def __eq__(self, other):
        """
        Converts = to !=
        """
        if self.__num == other:
            return False
        else:
            return True

    def __ne__(self, other):
        """
        Converts != to ==
        """
        if self.__num != other:
            return True
        elif self.__num == other:
            return False

    def __str__(self):
        """
        Prints to output
        """
        return "{}".format(self.__num)

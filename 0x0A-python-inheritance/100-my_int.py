#!/usr/bin/python3
"""
Module that creates the MyInt class
"""
class MyInt:
    """
    Implements the inversion of the == and =! operators
    """
    def __eq__(self, other):
        """
        Converts = to !=
        """
        if self == other:
            return False
        else:
            return True

    def __ne__(self, other):
        """
        Converts != to ==
        """
        if self != other:
            return True
        else:
            return False

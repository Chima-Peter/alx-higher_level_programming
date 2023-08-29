#!/usr/bin/python3
"""Creates a class Square that's based on 0-square.py"""


class Square:
    """Defines a class that's initialised with a private attribute"""

    def __init__(self, size):
        """Initialises attributes for the Square class. It validates
        size argument by checking TypeError and ValueError
    Args:
        size: the size of the square and set to 0 by default
        """
        try:
            if type(size) == int:
                if size > 0:
                    self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

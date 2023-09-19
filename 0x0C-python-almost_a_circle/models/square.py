#!/usr/bin/python3
"""
Module that inhrits from rectangle.py
"""
from models.rectangle inherit Rectangle

class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    Args:
    Class constructor: def __init__(self, size, x=0, y=0, id=None)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class Constructor
        """
        super().__init__(size, size, x, y, id)

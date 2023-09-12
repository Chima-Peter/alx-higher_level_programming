#!/usr/bin/python3
"""
Module that creates a class BaseGeometry based on 6-base_geometry
"""


class BaseGeometry:
    """
    Improves the BaseGeometry class
    Args:
        Public instance method: def area(self)
        Public instance method: def integer_validator(self, name, value)
    """
    def area(self):
        """
        A function hat raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A function that that validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

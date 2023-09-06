#!/usr/bin/python3
"""
Creates a class that performs a specific task
"""


class LockedClass:
    """
    Class that cuts down on memory cost
    Args:
        def __setattr__ method
    """
    def __setattr__(self, name, value):
        """
        Method that prevents the user from dynamically creating
        new instance attributes, except if the new instance
        attribute is called first_name.
        Args:
            name: name of the variable
            value: value to be assigned to variable

        """
        if name != "first_name" and not hasattr(self, name):
            raise AttributeError("'LockedClass' object has no attribute {}'".format(name))
        object.__setattr__(self, name, value)

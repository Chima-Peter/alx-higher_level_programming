#!/usr/bin/python3
"""
Module that inhrits from rectangle.py
"""
from models.rectangle import Rectangle

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

    def __str__(self):
        """
        Return string format
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,\
                self.y, self.width)

    @property
    def size(self):
        """
        width getter
        """
        return self.width
    @size.setter
    def size(self, value):
        """
        Width Setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """
        Assigns each argument to each attribute
        """
        my_list = [self.id, self.width,\
                self.x, self.y]
        for i in range(len(args)):
            my_list[i] = args[i]
        self.id = my_list[0]
        self.width = my_list[1]
        self.x = my_list[2]
        self.y = my_list[3]

        if len(args) == 0:
            my_dict = {'id': self.id, 'size': self.width,\
                    'x': self.x, 'y': self.y}
            for key in kwargs:
                my_dict[key] = kwargs[key]
            self.id = my_dict['id']
            self.width = my_dict['size']
            self.x = my_dict['x']
            self.y = my_dict['y']

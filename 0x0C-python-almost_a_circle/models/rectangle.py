#!/usr/bin/python3
"""
Module that creates clss Rectangle to inherit from Base
"""
Base = __import__('base').Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    Args:
        Private instance attribute: width, height, x and y
        Class constructor __init__
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
            Call the super class with id
            Assign each argument their right attribute
        """
        self.__width = width
        self.__height = height
        self__x = x
        self.__y = y
        super().__init__(self, id)

   @property
   def width(self):
       """
       Getter for width
       """
       return self.__width
   @width.setter
   def width(self, value):
       if type(value) is not int:
           raise TypeError("width must be an integer")
       self.__width = value

   @property
   def height(self):
       """
       Getter for height
       """
       return self.__height
   @height.setter
   def height(self, value):
       if type(value) is not int:
           raise TypeError("height must be an integer")
       self.__height = value

   @property
   def x(self):
       """
       Getter for x
       """
       return self.__x
   @x.setter
   def x(self, value):
       if type(value) is not int:
           raise TypeError("x must be an integer")
       self.__x = value

   @property
   def y(self):
       """
       Getter for y
       """
       return self.__y
   @y.setter
   def y(self, value):
       if type(value) is not int:
           raise TypeError("y must be an integer")
       self.__y = value

#!/usr/bin/python3
class Square:
    '''Creates a class yo return square area with getter and setter'''
    def __init__(self, size=0):
        '''Creates a function for initialization'''
        self.size = size
    @property
    def size(self):
        '''Gets the size to standard output'''
        return self.__size
    @size.setter
    def size(self, value):
        '''Sets the size to value'''
        if type(value) != int:
            '''Checks for integer'''
            raise TypeError("size must be an integer")
        elif value < 0:
            '''Checks for negative numbers'''
            raise ValueError("size must be >= 0")
        else:
            '''Appends value to size'''
            self.__size = value
    def area(self):
        '''Returns the current square area'''
        self.area = self.__size ** 2
        return self.area

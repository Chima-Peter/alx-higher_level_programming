#!/usr/bin/python
'''This module creates a class and measures its area using its square'''
class Square:
    '''Creates a class that returns the current square area'''
    def __init__(self, size):
        '''Initialises the class square'''
        if type(size) != int:
            '''Checks for int'''
            raise TypeError("size must be an interger")
        elif size < 0:
            '''Checks for negaitive numbers'''
            raise ValueError("size must be >= 0")
        else:
            '''Appends size to size'''
            self.__size = size
    def area(self):
            '''Returns the current sqy=uare area'''
            self.area = self.__size ** 2
            return self.area

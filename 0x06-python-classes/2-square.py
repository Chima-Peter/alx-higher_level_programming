#!/usr/bin/python3
class Square:
    ''' This class defines a square with a private instance attribute of optional value and also does some other checks'''
    def __init__(self, size=0):
        '''This function initialises the square class with size attribute'''
        if type(size) != int:
            ''' Checks for interger'''
            raise TypeError("size must be an interger")
        elif size < 0:
            ''' Checks if size is lower than 0'''
            raise ValueError("size must be >= 0")
        else:
            '''Initialises the size to size'''
            self.__size = size

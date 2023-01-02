#!/usr/bin/python3
'''This module creates a class that defines a square based on its size'''
class Square:
    ''' This class defines a square based on its size which must be a private instance attribute.'''
    def __init__(self, size):
        '''This initialises the class square'''
        self.__size = size

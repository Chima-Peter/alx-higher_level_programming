#!/usr/bin/python3
'''This module creates a class to compare squares of different instannces of samwe class'''
class Square:
    '''Creates a class to compare instances'''
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
    def __eq__(self, other):
        '''This method compares 2 squares to see if they're equal'''
        if self.__size == other.__size:
            '''returns true if it is'''
            return True
        else:
            '''returns false if not'''
            return False
    def __lt__(self, other):
        '''Compares 2 squares to see if the first is lesseer that second'''
        if self.__size < other.__size:
            '''returns true if it is'''
            return True
        else:
            '''Returns false if not'''
            return False
    def __le__(self, other):
        '''Compares 2 squares if the 1st is equal or lesser than the 2nd'''
        if self.__size <= other.__size:
            '''returrns true if it is'''
            return True
        else:
            '''returns false if not'''
            return False
    def __gt__(self, other):
        '''Compares 2 squares if the 1st is greater trhan the 2nd'''
        if self.__size > other.__size:
            '''returns true if it is'''
            return True
        else:
            '''returns false if not'''
            return False

        def __ge__(self, other):
            '''Compares 2 squares to see if the 1st is greater than or equal to the 2nd'''
            if self.__size >= other.__size:
                '''returns true if it is'''
                return True
            else:
                '''returns false if not'''
                return False
        def __ne__(self, other):
            '''Compares 2 squares to see if they're not equal'''
            if self.__size != other__size:
                '''returns true if it is'''
                return True
            else:
                '''returns false if not'''
                return False

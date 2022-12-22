#!/usr/bin/python3
class Square:
    '''Creates a class'''
    def __init__(self, size):
        '''Initialises the class with a value'''
        self.size = size
    @property
    def size(self):
        '''Gets the value of size'''
        return self.__size
    @size.setter
    def size(self, value):
        '''Sets the value of self to a new value'''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            '''Appends value of value to size'''
            self.__size = value
    def area(self):
        '''Returns current size square'''
        self.area = self.__size ** 2
        return self.area
    def my_print(self):
        '''Prints in stdout the square with #'''
        if self.__size == 0:
            '''Prints straight line if size == 0'''
            print()
        else:
            for i in range(self.__size):
                '''Range to print # vertically'''
                for n in range(self.__size):
                    '''Range to print # horizontally'''
                    print("#", end="")
                print()

#!/usr/bin/python3
'''This module creates a class that prints human-readable code when the print function is called
class Square:
    '''Creates a class to print directly from str'''
    def __init__(self, size=0, position=(0,0)):
        '''Initialises the class with a value'''
        self.size = size
        self.position = position
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
    @property
    def position(self):
        '''Gets the new value of the position tuple'''
        return self.__position
    @position.setter
    def position(self, value):
        '''Sets the new value of the position tuple'''
        if type(value[0]) != int or type(value[1]) != int:
            '''checks for integers'''
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            '''Checks for positive numbers'''
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
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
            '''prints when self.__size != 0'''
            n = 0
            if self.__position[0] <= self.__position[1]:
                '''sets the length of self.__position'''
                n = self.__position[1]
            else:
                '''sets the length of self.__position'''
                n = self.position[0]
            for i in range(self.__size):
                '''Number of times to print'''
                for x in range(n):
                    '''Range to print " "'''
                    print(" ", end="")
                for s in range(self.__size):
                    '''Range to print #'''
                    print("#", end="")
                print()
    def __str__(self):
        '''Prints code inside here whenever the class is called ny str or print'''
        '''Prints in stdout the square with #'''
        if self.__size == 0:
            '''Prints straight line if size == 0'''
            print()
        else:
            '''prints when self.__size != 0'''
            n = 0
            if self.__position[0] <= self.__position[1]:
                '''sets the length of self.__position'''
                n = self.__position[1]
            else:
                '''sets the length of self.__position'''
                n = self.position[0]
            for i in range(self.__size):
                '''Number of times to print'''
                for x in range(n):
                    '''Range to print " "'''
                    print(" ", end="")
                for s in range(self.__size):
                    '''Range to print #'''
                    print("#", end="")
                print()
        return ""

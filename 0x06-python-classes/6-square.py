#!/usr/bin/python3
class Square:
    ''''Creates a class '''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialises the class with size and position'''
        self.size = size
        self.position = position
    @property
    def size(self):
        '''Gets self.__size'''
        return self.__size
    @size.setter
    def size(self, value):
        '''Sets the new value of size'''
        if type(value) != int:
            '''Checks for integer'''
            raise TypeError("size must be an integer")
        elif value < 0:
            '''Checks for negative numbers'''
            raise ValueError("size must be >= 0")
        else:
            '''Changes the value of size'''
            self.__size = value
    @property
    def position(self):
        '''Gets self.__position'''
        return self.__position
    @position.setter
    def position(self, value):
        '''Sets the new value of position tuple'''
        if type(value[0]) or type(value[1]) != int:
            '''Checks if both tuple members are integers'''
            #raise TypeError("position must be a tuple of 2 intergers")
            print("jd")
        else:
            '''Sets the new value of position elements'''
            self.__position = value
    def area(self):
        '''Returns the current square area'''
        self.area = self.__size ** 2
        return self.area
    def my_print(self):
        '''Prints size and position in form of ' ' and #'''
        for i in range(self.__size):
            '''Range of size vertically'''
            if self.__position[0] == 0:
                '''Size of a for the tuple range'''
                a = self.__position[1]
            elif self.__position[1] == 0:
                '''Size of a for the tuple range'''
                a = self.__position[0]
            else:
                '''Size of a for the tuple range'''
                a = 0
            for n in range(a):
                print(" ", end="")
            for v in range(self.__size):
                print("#", end="")
            print()

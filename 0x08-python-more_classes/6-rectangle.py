#!/usr/bin/python3
"This module creates a class that measures the perimeter and area of a rectangle and counts the jumber of instances created and deleted"
class Rectangle:
    "The class to be measured in both it's area and rectangle"
    number_of_instances = 0
    def __init__(self, width, height):
        "This function initialises the attributes"
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
    @property
    def width(self):
        "Gets the new value of width"
        return self.__width
    @width.setter
    def width(self, value):
        "Sets the new value of width"
        if type(value) != int:
            "Checks if value is an integer"
            raise TypeError("width must be an integer")
        elif value < 0:
            "Checks if value if less than 0"
            raise ValueError("width must be >= 0")
        else:
            "Sets the new value of width if all checks were passed"
            self.__width = value
    @property
    def height(self):
        "This function gets the new value of heihght"
        return self.__height
    @height.setter
    def height(self, value):
        "This function sets the new value for height"
        if type(value) != int:
            "Checks if value if of type int"
            raise TypeError("height must be an integer")
        elif value < 0:
            "Checks if value is > 0"
            raise ValueError("height must be >= 0")
        else:
            "Sets value if all checks were met"
            self.__height = value
    def area(self):
        "This function returns the area of a rectangle"
        return self.__width * self.__height
    def perimeter(self):
        "This function returns the perimeter of a rectangle"
        if self.__width == 0 or self.__height == 0:
            "Checks that both values are > 0"
            return 0
        per = 2 * (self.__width + self.__height)
        return per
    def __str__(self):
        "This function prints in # format the rectangle whenever str or print function is called"
        if self.__width == 0 or self.__height == 0:
            "Prints empty line if either attribute == 0"
            print()
            return ""
        else:
            "Else, it prints # in form of rectangle"
            for i in range(self.__height):
                "Prints the height of the rectangle"
                for n in range(self.__width):
                    "Prints the width of the rectangle"
                    print("#", end="")
                if i < (self.height - 1):
                    "Prints breakline except on last line"
                    print()
            return ""
    def __repr__(self):
        "This function returns a trsing representation of the rectangle"
        return f"Rectangle({self.__width}, {self.__height})"
    def __del__(self):
        "Prints message when an object is deleted"
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

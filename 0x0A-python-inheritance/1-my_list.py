#!/usr/bin/python3
"""
Module that creates the MyList class
"""


class MyList(list):
    """
    A class that inheurts from list
    """
    def __init__(self):
        self.my_list = super().__init__()
    def print_sorted(self):
        """
        Sorts a list
        """
        #MyList.my_list.sort()
        print("{}".format(self.my_list))

#!/usr/bin/python3
"""
Module that creates the MyList class
"""


class MyList(list):
    """
    A class that inheurts from list
    """
    my_list = list
    def print_sorted(self):
        """
        Sorts a list
        """
        MyList.my_list.sort()
        print("{}".format(self.my_list))

#!/usr/bin/python3
"""
Module tha creates the append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts a line of text to a file, after\
            each line containing a specific string
    """
    with open(filename, 'w+', encoding='utf-8') as f:
        line = f.readline

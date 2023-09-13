#!/usr/bin/python3
"""
Module for the def write_file function
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8) and returns the number of characters written
    """
    with open(filename, 'r+', encoding='utf-8') as f:
        return f.write(text)

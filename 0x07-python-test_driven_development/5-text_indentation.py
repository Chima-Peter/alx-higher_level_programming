#!/usr/bin/python3
"""
Write a function that indents a text
"""


def text_indentation(text):
    """
    Write a function that prints a text with 2 new lines \
            after each of these characters: ., ? and :
    """
    new = ""
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(new)
            new = ""
        new += i

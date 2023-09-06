#!/usr/bin/python3
"""
Write a function that indents a text
"""


def text_indentation(text):
    """
    Write a function that prints a text with 2 new lines \
            after each of these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    new_list = []
    new = ""
    count = 0
    for row in text:
        new += row
        if row == "." or row == ":" or row == "?":
            new_list.append(new)
            count += len(new)
            new = ""
    new_list.append(text[count:])
    i = 0
    for row in new_list:
        i += 1
        print("{}".format(row.strip()), end="")
        if i < len(new_list):
            print()
            print()

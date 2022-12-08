#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = []
    for i, n in a_dictionary.items():
        if n == value:
            temp.append(i)
    for i in temp:
        del a_dictionary[i]
    return a_dictionary

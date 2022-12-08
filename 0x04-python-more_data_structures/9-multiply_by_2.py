#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i, n in a_dictionary.items():
        c = n * 2
        new_dictionary[i] = c
    return new_dictionary

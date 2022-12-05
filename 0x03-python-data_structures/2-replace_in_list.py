#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    n = 0
    num = len(my_list)
    arr = []
    if idx >= 0 and idx < num:
        my_list[idx] = element
        return my_list
    else:
        return my_list

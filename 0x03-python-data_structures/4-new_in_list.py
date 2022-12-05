#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    num = len(my_list)
    if idx >= 0 and idx < num:
        for i in my_list:
            new.append(i)
        new[idx] = element
        return new
    else:
        return my_list

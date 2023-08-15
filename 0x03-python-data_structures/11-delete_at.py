#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list
    my_list = []
    for i in range(0, len(new_list)):
        if i != idx:
            my_list.append(new_list[i])
    return my_list

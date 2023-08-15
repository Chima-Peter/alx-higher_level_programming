#!/usr/bin/python3
def max_integer(my_list=[]):
    max_no = 0
    for i in range(0, len(my_list)):
        if max_no - my_list[i] >= 0:
            max_no = max_no
        else:
            max_no = my_list[i]
    return max_no

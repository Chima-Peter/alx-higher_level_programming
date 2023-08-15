#!/usr/bin/python3
def max_integer(my_list=[]):
    max_no = my_list[i]
    for i in range(0, (len(my_list) - 1)):
        if max_no - my_list[i + 1] >= 0:
            max_no = my_list[i]
        else:
            max_no = my_list[i + 1]
    return max_no

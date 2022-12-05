#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    num = len(my_list)
    count = 1
    for i in my_list:
        n = num - count
        print("{}".format(my_list[n]))
        count += 1

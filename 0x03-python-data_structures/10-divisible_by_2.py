#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp = []
    for n in my_list:
        if n % 2 == 0:
            i = True
        else:
            i = False
        temp.append(i)
    return temp

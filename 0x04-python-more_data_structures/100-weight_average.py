#!/usr/bin/python3
def weight_average(my_list=[]):
    x = 0
    div = 0
    for i in my_list:
        c = 1
        for n in i:
            c = c * n
        x = x + c
        for a, b in enumerate(i):
            if a == 1:
                div = div + b
    weight = x / div
    return weight

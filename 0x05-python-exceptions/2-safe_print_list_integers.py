#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    counter = 0
    for i in my_list:
        count += 1
    if x >= count:
        x = count
    for i in my_list:
        if i <= x:
            if type(i) == int:
                try:
                    print(i, end="")
                    counter += 1
                except IndexError as e:
                    print(e)
    print()
    return counter

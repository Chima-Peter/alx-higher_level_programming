#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        count += 1
    if x >= count:
        x = count
    for i in my_list:
        if i <= x:
            try:
                print(i, end="")
            except IndexError as e:
                print(e)
    print()
    return x

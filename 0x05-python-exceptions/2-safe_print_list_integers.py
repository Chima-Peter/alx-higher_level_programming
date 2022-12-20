#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for n in my_list:
        i = i + 1
    n = 0
    for num, new in enumerate(my_list):
        if num < x:
            try:
                if new / 1 == new:
                    print("{:d}".format(new), end="")
                    n = n + 1
            except TypeError:
                pass
    print()
    return n

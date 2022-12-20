#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new_list = []
    i = 0
    for n in my_list:
        i = i + 1
    if x > i:
        x = i
    try:
        for num, new in enumerate(my_list):
            if num < x:
                print("{}".format(new), end="")
        print()
    except Exception as e:
        print(e)
    return x

#!/usr/bin/python3
def element_at(my_list, idx):
    n = 0
    num = len(my_list)
    if idx >= 0 and idx < num:
        for i in my_list:
            if idx == n:
                return i
            n += 1
    else:
        return None

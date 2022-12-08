#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = set()
    for i in set_1:
        for n in set_2:
            if i is n:
                new.add(i)
    return new

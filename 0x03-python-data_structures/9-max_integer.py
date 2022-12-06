#!/usr/bin/python3
def max_integer(my_list=[]):
    num = len(my_list)
    if num == 0:
        return None
    else:
        for i in range(0, num):
            count = 0
            for n in my_list:
                if my_list[i] - n >= 0:
                    count += 1
                else:
                    break
            if count == num:
                return my_list[i]

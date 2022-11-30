#!/usr/bin/python3
def pow(a, b):
    n = a
    c = b + 1
    if b > 0:
        for i in range(2, c):
            a = a * n
        return a
    elif b < 0:
        for i in range(b, 1):
            a = a / n
        return a
    elif b == 1:
        return a
    else:
        return 1

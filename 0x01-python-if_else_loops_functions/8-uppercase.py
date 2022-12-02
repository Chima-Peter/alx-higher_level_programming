#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = ord(i) - 32
            n = chr(i)
            str1 += n
        else:
            str1 += i
    print("{}".format(str1))

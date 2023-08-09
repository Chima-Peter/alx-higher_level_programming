#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            new = ord(i) - 32
        else:
            new = ord(i)
        print("{}".format(chr(new)), end="")
    print()

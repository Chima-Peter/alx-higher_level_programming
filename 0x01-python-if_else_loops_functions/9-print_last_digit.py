#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    num = number % 10
    if num < 0:
        num = -num
    print("{}".format(num), end="")
    return num

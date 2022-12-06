#!/usr/bin/python3
def multiple_returns(sentence):
    num = len(sentence)
    if num > 0:
        first = sentence[0]
        new_tuple = (num, first)
        return new_tuple
    else:
        first = None
        new_tuple = (num, first)
        return new_tuple

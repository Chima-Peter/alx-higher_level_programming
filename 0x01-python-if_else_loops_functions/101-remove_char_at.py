#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    word = ''
    def remove_char_at(str, n):
        if x != n:
            word += str[x]
        x += 1
        return word

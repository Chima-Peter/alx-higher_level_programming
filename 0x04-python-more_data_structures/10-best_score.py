#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        num = len(a_dictionary)
        for i, n in a_dictionary.items():
            count = 0
            for x, y in a_dictionary.items():
                if n - y >= 0:
                    count += 1
                else:
                    count -= 1
            if count == num:
                return i

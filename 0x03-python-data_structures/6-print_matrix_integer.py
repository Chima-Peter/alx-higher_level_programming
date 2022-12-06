#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new = []
    for i in matrix:
        x = 0
        for n in i:
            print("{:d}".format(n), end=" " if x < 2 else "")
            x += 1
        print()
#    print(len(matrix)

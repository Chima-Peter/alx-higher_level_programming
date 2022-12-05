#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new = []
    for i in matrix:
        x = 0
        for n in i:
            print("{}".format(n), end="")
            x += 1
            if x < 3:
                print(end=" ")
        print()
#    print(len(matrix)

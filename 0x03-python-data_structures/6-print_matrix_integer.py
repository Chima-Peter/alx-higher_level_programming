#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new = []
    for n in range(3):
        new.append([i[n] for i in matrix])
    print("{}".format(new))

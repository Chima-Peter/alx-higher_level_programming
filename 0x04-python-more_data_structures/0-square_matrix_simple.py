#!usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        for n in i:
            x = n ** 2
            new.append(x)
    return new

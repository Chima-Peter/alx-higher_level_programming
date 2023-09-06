#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
Prototype: def matrix_divided(matrix, div):
"""
def matrix_divided(matrix, div):
    """
    Function to divide all elements of the matrix by div
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    auto = len(matrix[0])
    for i in range(1, len(matrix)):
        if auto != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        auto = len(matrix[i])
    for row in matrix:
        for i in row:
            print(i)

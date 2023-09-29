#!/usr/bin/python3
"""this module devides a matrix by a number, For example
matrix_devided([2,4,6], 2)
[1,2,3]"""


def matrix_divided(matrix, div):
    """devides a matrix by a number"""
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    rows_len = []
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists) \
    of integers/floats")
        rows_len.append(len(i))
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    for p in rows_len:
        if p != rows_len[0]:
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]

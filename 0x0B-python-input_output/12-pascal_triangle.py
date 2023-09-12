#!/usr/bin/python3
"""a function to return Pascal's triangle"""


def pascal_triangle(n):
    """returns list containing Pascal's triangle of len n"""
    pascal_triangle = []
    last = [1]
    if n <= 0:
        return pascal_triangle
    for row_number in range(n):
        row_list = []
        if row_number == 0:
            row_list = [1]
        else:
            for i in range(row_number + 1):
                if i == 0:
                    row_list.append(0 + last[i])
                elif i == (row_number):
                    row_list.append(last[i - 1] + 0)
                else:
                    row_list.append(last[i - 1] + last[i])
        last = row_list
        pascal_triangle.append(row_list)
    return pascal_triangle

#!/usr/bin/python3
"""Task 2"""


def matrix_divided(matrix, div):
    """The following line creates a set of row lengths included in matrix"""
    """If its length is not equal to 1 it means rows have different lengths"""
    if len({len(list) for list in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for list in matrix:
        for number in list:
            if type(number) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)" +
                " of integers/floats")
    return [[float("{:.2f}".format(x/div)) for x in list] for list in matrix]

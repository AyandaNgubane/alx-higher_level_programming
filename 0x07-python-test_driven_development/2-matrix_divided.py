#!/usr/bin/python3

"""Write a function that divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any module"""


def matrix_divided(matrix, div):
    """
    divides all elements of matrix
    args:
        matrix - matrix
        div - divisor
    Returns: new matrix
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if (type(div) is not int and type(div) is not float) or div != div:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    len_row = 0
    new_list = []

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len_row == 0:
            len_row = len(row)
        if len_row != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        new_row =[]

        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                new = elem / div
                new = round(new, 2)
                new_row.append(new)
        new_list.append(new_row)
    return (new_list)

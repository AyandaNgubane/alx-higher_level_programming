#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    sqrd = list(map(lambda row: list(map(lambda x: x * x, row)), new_matrix))
    return (sqrd)

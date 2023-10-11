#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    #new_matrix = matrix.copy()
    return list(map(lambda row: list(map(lambda x: x * x, row)), matrix))

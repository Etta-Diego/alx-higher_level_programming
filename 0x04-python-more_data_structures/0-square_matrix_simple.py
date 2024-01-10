#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [[element ** 2 for element in row] for row in matrix]
    return squares

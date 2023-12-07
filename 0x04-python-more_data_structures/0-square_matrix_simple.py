#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_val = []
    for row in matrix:
        squared_val.append([c**2 for c in row])
    return squared_val


#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tmp = []

    for r in matrix:
        tmp.append(list(map(lambda r: r ** 2, r)))
    return (tmp)

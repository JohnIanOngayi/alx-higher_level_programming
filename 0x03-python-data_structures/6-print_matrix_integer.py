#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    length = len(matrix)

    for i in range(0, length):
        lem = len(matrix[i])
        for j in range(0, lem):
            if j != lem - 1:
                print("{0:d} ".format(matrix[i][j]), end='')
            else:
                print("{0:d}".format(matrix[i][j]))

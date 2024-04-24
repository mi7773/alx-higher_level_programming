#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    if matrix is None:
        print()
    for row in matrix:
        for i in row:
            print("{}".format(i), end=" ")
        print()

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_matrix = [[i ** 2 for i in j] for j in matrix]
    return new_matrix

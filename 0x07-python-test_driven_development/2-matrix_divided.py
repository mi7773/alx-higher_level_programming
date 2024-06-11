#!/usr/bin/python3

"""
2-matrix_divided module.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): The first parameter
        div (int, float): The second parameter

    Returns:
        list: The return of the function
    """
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    if len(matrix) == 0:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    result = []
    for row in matrix:
        sub_res = []
        for element in row:
            sub_res.append(round((element / div), 2))
        result.append(sub_res)
    return result

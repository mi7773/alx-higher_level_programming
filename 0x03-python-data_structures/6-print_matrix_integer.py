#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for i in matrix:
        k = len(i)
        for j in range(k):
            if j < k - 1:
                print("{:d}".format(i[j]), end=' ')
            else:
                print("{:d}".format(i[j]))

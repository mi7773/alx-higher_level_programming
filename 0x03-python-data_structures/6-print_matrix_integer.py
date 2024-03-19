#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    l = len(matrix)
    for i in range(l):
        ll = len(matrix[i])
        for j in range(ll):
            if j < ll - 1:
                print(f"{matrix[i][j]:d}", end=' ')
            else:
                print(f"{matrix[i][j]:d}")

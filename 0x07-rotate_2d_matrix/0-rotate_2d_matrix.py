#!/usr/bin/python3
""" 2D matrix rotation """


def rotate_2d_matrix(matrix):
    """ rotates the matrix 90 degrees"""
    matrix_size = len(matrix)
    for m in range(matrix_size):
        for n in range(m):
            temp = matrix[m][n]
            matrix[m][n] = matrix[n][m]
            matrix[n][m] = temp
    for m in range(matrix_size):
        matrix[m].reverse()

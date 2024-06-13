#!/usr/bin/python3
"""
Rotate 2D Matrix module
"""

from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Rotate a 2D matrix 90 degrees clockwise in place.

    :param matrix: List of lists, where each inner list represents
    a row in the matrix.
    :return: None. The matrix is modified in place.
    """
    n = len(matrix)

    """ Step 1: Transpose the matrix """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    """ Step 2: Reverse each row """
    for i in range(n):
        matrix[i].reverse()


def print_matrix(matrix: List[List[int]]) -> None:
    """
    Print a 2D matrix in a formatted way.

    :param matrix: List of lists, where each inner list represents
    a row in the matrix.
    :return: None. The matrix is printed row by row.
    """
    for row in matrix:
        print(row)

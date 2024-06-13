#!/usr/bin/python3
"""
Rotate 2D Matrix module
"""

from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Rotate a 2D matrix 90 degrees clockwise in place.
    
    :param matrix: List of lists, where each inner list
    represents a row in the matrix.
    :return: None. The matrix is modified in place.
    """
    n = len(matrix)
    
    """ Step 1: Transpose the matrix """
    for e in range(n):
        for m in range(e, n):
            matrix[e][m], matrix[m][e] = matrix[m][e], matrix[e][m]
    
    """ Step 2: Reverse each row """
    for e in range(n):
        matrix[e].reverse()


def print_matrix(matrix: List[List[int]]) -> None:
    """
    Print a 2D matrix in a formatted way.
    
    :param matrix: List of lists, where each inner list represents a row in the matrix.
    :return: None. The matrix is printed row by row.
    """
    for row in matrix:
        print(row)


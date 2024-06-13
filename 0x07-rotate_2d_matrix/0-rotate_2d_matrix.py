#!/usr/bin/python3

"""
Rotate 2D Matrix module
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix clockwise by 90 degrees.

    Args:
        matrix (List[List[int]]): The input matrix to be rotated.

    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix[0])

    """ Iterate over the columns of the matrix starting from the last one."""
    for m in range(n - 1, -1, -1):
        for e in range(0, n):
            matrix[e].append(matrix[m].pop(0))

#!/usr/bin/python3

import math

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows for Pascal's triangle.

    Returns:
        list of lists of integers: Pascal's triangle.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    triangle = []

    for row_num in range(n):
        row = []
        for k in range(row_num + 1):
            coefficient = math.comb(row_num, k)
            row.append(coefficient)
        triangle.append(row)

    return triangle

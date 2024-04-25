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
    try:
        # Error and Exception Handling
        if not isinstance(n, int) or n <= 0:
            raise ValueError(f"n must be positive integer, but received: {n}")
    except TypeError:
        raise TypeError("Input must be an integer")

    triangle = []

    for row_num in range(n):
        # Lists and List Comprehensions
        # Utilizing list comprehension for generating each row
        row = [math.comb(row_num, k) for k in range(row_num + 1)]
        triangle.append(row)

    return triangle

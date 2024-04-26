#!/usr/bin/python3

def generate_pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows for Pascal's triangle.

    Returns:
        list of lists of integers: Pascal's triangle.
    """
    if n < 0:
        raise ValueError(f"n must be a non-negative integer, but received: {n}")

    triangle = []

    for row_num in range(n):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            if row_num - 1 < len(triangle) and j - 1 < len(triangle[row_num - 1]):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)

    return triangle
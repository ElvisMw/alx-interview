#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows for Pascal's triangle.

    Returns:
        list of lists of integers: Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for e in range(1, n):
        row = [1]
        for m in range(1, e):
            row.append(triangle[e - 1][m - 1] + triangle[e - 1][m])
        row.append(1)
        triangle.append(row)

    return triangle

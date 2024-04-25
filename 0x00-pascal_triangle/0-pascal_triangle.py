#!/usr/bin/env python3

def pascal_triangle(n):
    """
    Returns the first n rows of Pascal's triangle as a list of lists of integers.

    n must be a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    triangle = []

    for row_num in range(n):
        """ Add a new row to the Pascal triangle """
        row = [1]

        for j in range(1, row_num):
            """ Calculate the value of the next element in the row """
            element = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            row.append(element)

        if row_num > 0:
            """ Add a 1 to the end of the row (to make the rows identical to
             Pascal's triangle) """
            row.append(1)

        triangle.append(row)

    return triangle


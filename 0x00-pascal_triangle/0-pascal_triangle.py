#!/usr/bin/python3

def pascal_triangle(n):
    """
    Computes the n-th row of Pascal's triangle.

    Parameters
    ----------
    n : int
        The row number, 0-indexed.

    Returns
    -------
    list
        The n-th row of Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        """ Compute the i-th row of Pascal's triangle """

        row = [1]
        for j in range(1, i):
            """ The (i, j)-th entry of Pascal's triangle is
            the sum of the (i-1, j-1)
            and (i-1, j) entries """
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

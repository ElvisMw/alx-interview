#!/usr/bin/python3

"""
Generate Pascal's triangle.

Pascal's triangle is a triangular array of numbers.
It is constructed with the following rules:

* The first row consists of one 1.
* Each subsequent row is constructed by adding the number above
and to the left to the number above and to the right.
* The process is repeated until the desired number of rows is reached.

Arguments:
    n (int): Number of rows in the Pascal's triangle.

Returns:
    List[List[int]]: A Pascal's triangle of size n.

Raises:
    ValueError: If n is a negative integer.

"""


def pascal_triangle(n):
    """Generate Pascal's triangle.

    Args:
        n (int): Number of rows in the Pascal's triangle.

    Returns:
        List[List[int]]: A Pascal's triangle of size n.

    Raises:
        ValueError: If n is a negative integer.

    """
    if n < 0:
        raise ValueError(f"n must be a non-negative integer, but got: {n}")

    triangle = []

    for rowNm in range(n):
        """ Create a row (rowNm) of n ones """
        row = [1] * (rowNm + 1)
        """ Calculate the values of the row using the rule """
        for e in range(1, rowNm):
            if rowNm - 1 < len(triangle) and e - 1 < len(triangle[rowNm - 1]):
                row[e] = triangle[rowNm - 1][e - 1] + triangle[rowNm - 1][e]
        """ Append the row to the triangle """
        triangle.append(row)

    return triangle

#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows for Pascal's triangle.

    Returns:
        list of lists of integers: Pascal's triangle.
    """
    try:
        if not isinstance(n, int) or n <= 0:
            raise ValueError(f"n must be a positive integer, but received: {n}")
    except TypeError:
        raise TypeError("Input must be an integer")

    triangle = []

    for row_num in range(n):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    # Test cases
    tests = [5, 1, 0, 10, 100]
    for test in tests:
        print(f"Pascal's triangle for n = {test}:")
        for row in pascal_triangle(test):
            print(row)
        print()
#!/usr/bin/python3

"""
Given a positive integer e, find the minimum number of operations needed to
reduce e to 1 using the following operations:

1. If the number is even, divide it by 2.
2. If the number is odd, multiply it by 3 and add 1.

For example, to reduce 7 to 1, you can use the
following sequence of operations:
7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 ->
5 -> 16 -> 8 -> 4 -> 2 -> 1
"""


def minOperations(e):
    """
    Find the minimum number of operations needed to reduce e to 1.

    Args:
        e: A positive integer

    Returns:
        The minimum number of operations needed to reduce e to 1
    """
    if e <= 1:
        return 0
    for op in range(2, e+1):
        if e % op == 0:
            return minOperations(int(e/op)) + op

#!/usr/bin/python3
""" Making Change"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determine the fewest number of coins needed to meet a
	given total amount.

    :param coins: List of the values of the coins in your possession
    :param total: The total amount to meet with coins
    :return: Fewest number of coins needed to meet total, or
	-1 if it's not possible
    """
    if total <= 0:
        return 0

    """ Initialize DP array with an initial value of total
	+ 1, which is impossible high """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    """ Populate the DP array """
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

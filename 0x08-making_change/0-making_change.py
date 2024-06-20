#!/usr/bin/python3
""" Making Change """
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
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    e = len(coins)
    while rem > 0:
        if coin_idx >= e:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count

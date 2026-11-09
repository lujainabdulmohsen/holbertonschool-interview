#!/usr/bin/python3
"""Minimum number of coins to make change."""


def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in set(coins):
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return -1 if dp[total] == float('inf') else dp[total]

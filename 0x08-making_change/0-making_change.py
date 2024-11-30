#!/usr/bin/python3
"""Calculate the minimum number of coins needed to make up a given total."""


def makeChange(coins, total):
    """
    This function uses dynamic programming to find the minimum number of coins
    required to make a specific amount using a list of
    available coin denominations.

    Parameters:
    coins (list of int): A list of available coin denominations.
    total (int): The target amount for which the change needs to be made.

    Returns:
    int: The minimum number of coins needed to make the total, or -1 if it is
         not possible to make the total with the available coins.
    """
    # If total is 0 or negative, no coins are needed
    if total <= 0:
        return 0

    # Initialize the dp array with infinity for all values except dp[0]
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Loop through each coin in the list of coins
    for coin in coins:
        # For each possible amount from the coin's value up to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1 (it's
    # impossible to make the total)
    if dp[total] == float('inf'):
        return -1

    # Otherwise, return the minimum number of coins needed
    return dp[total]

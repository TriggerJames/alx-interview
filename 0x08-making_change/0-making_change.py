#!/usr/bin/python3

def makeChange(coins, total):
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Process each coin denomination
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the total cannot be made with the given coins, return -1
    return dp[total] if dp[total] != float('inf') else -1

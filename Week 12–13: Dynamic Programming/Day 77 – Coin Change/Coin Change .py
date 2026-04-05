def coinChange_debug(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], dp[a - coin] + 1)
        print(f"dp[{a}] ->", dp)

    return dp[amount] if dp[amount] != float('inf') else -1


print(coinChange_debug([1,3,4], 6))

#tc: O(n × amount) Sc:O(amount)
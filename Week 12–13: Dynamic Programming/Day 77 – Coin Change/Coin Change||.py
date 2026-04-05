from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Return the number of combinations to make 'amount' using given coins.
        """
        # dp[i] = number of ways to make amount i
        dp = [0] * (amount + 1)

        # Base case:
        # There is exactly 1 way to make amount 0 -> choose nothing
        dp[0] = 1

        # Iterate over each coin
        # Doing coins first ensures we count combinations, not permutations
        for coin in coins:

            # 'current_amount' represents the amount we are forming
            # Start from 'coin' because amounts less than 'coin' cannot include this coin
            for current_amount in range(coin, amount + 1):

                # dp[current_amount - coin] = number of ways to make the smaller amount
                # Adding current coin to all ways of making (current_amount - coin)
                # gives new ways to make current_amount
                dp[current_amount] += dp[current_amount - coin]

        # dp[amount] now contains total number of combinations
        return dp[amount]

# ---- Example Run ----
coins = [1, 2, 5]
amount = 5
sol = Solution()
print("Number of ways:", sol.change(amount, coins))  # Output: 4

# Time Complexity: O(n * amount), where n = number of coins
# Space Complexity: O(amount)
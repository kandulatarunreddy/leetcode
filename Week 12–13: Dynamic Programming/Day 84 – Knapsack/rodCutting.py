class Solution:
    def rodCutting(self, price, n):
        """
        price[i] = price of rod of length (i+1)
        n = total rod length

        dp[length] = maximum profit we can get from rod of size = length
        """

        dp = [0] * (n + 1)

        # Build solution from smaller rod lengths → bigger rod lengths
        for length in range(1, n + 1):

            # We are solving: "What is the best profit for rod of size = length?"

            # Try every possible FIRST CUT
            for cut in range(1, length + 1):

                # -------------------------------
                # cut = size of first piece we take
                #
                # remaining rod = length - cut
                #
                # profit =
                #   price of first piece
                #   + best profit from remaining rod
                # -------------------------------

                first_piece_value = price[cut - 1]
                remaining_profit = dp[length - cut]

                total_profit = first_piece_value + remaining_profit

                # Choose best among all possible cuts
                dp[length] = max(dp[length], total_profit)

                # 🔍 VERY IMPORTANT EXAMPLE:
                # Suppose:
                # length = 4
                # cut = 2
                #
                # Step:
                # First piece = length 2 → price[1] = 5
                # Remaining rod = 4 - 2 = 2
                # Best for remaining = dp[2] = 5
                #
                # Total = 5 + 5 = 10

        return dp[n]
if __name__ == "__main__":
    sol = Solution()

    price = [2, 5, 7, 8]
    n = 4

    print("Maximum Profit:", sol.rodCutting(price, n))

# Output: 10

# Time Complexity: O(n^2)
# Space Complexity: O(n)
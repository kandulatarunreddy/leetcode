# Ones and Zeroes (LeetCode 474)
# 0/1 Knapsack with 2 constraints (zeros and ones)

class Solution:
    def findMaxForm(self, strs, m, n):
        """
        strs: List[str] -> binary strings
        m: int -> max zeros allowed
        n: int -> max ones allowed

        dp[i][j] = maximum number of strings we can pick
                   using at most i zeros and j ones
        """

        # Create DP table initialized to 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # Example input:
        # strs = ["10","0001","111001","1","0"]
        # m = 5 (zeros), n = 3 (ones)

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            # Example:
            # s = "10" -> zeros = 1, ones = 1

            # IMPORTANT: iterate BACKWARD to avoid reusing same string
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):

                    # -----------------------------------------
                    # Option 1: DO NOT take this string
                    # dp[i][j] remains unchanged
                    #
                    # Option 2: TAKE this string
                    # Then we must have previously used:
                    #   (i - zeros) zeros
                    #   (j - ones) ones
                    #
                    # So we look at:
                    # dp[i - zeros][j - ones]
                    #
                    # Meaning:
                    # "Before picking this string, what was the best
                    # we could do with remaining capacity?"
                    #
                    # Then add this string (+1)
                    # -----------------------------------------

                    dp[i][j] = max(
                        dp[i][j],                         # don't take
                        1 + dp[i - zeros][j - ones]       # take
                    )

                    # 🔍 Example Walkthrough:
                    # Suppose i = 2, j = 2 and current string = "10"
                    # zeros = 1, ones = 1
                    #
                    # Option 2 uses:
                    # dp[2-1][2-1] = dp[1][1]
                    #
                    # If dp[1][1] = 1 (we formed 1 string before),
                    # then dp[2][2] = 1 + 1 = 2

        return dp[m][n]


# ---------------------- DRIVER CODE ----------------------

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3

    # Expected Output: 4
    # Explanation:
    # We can pick: "10", "0001", "1", "0"
    # zeros = 1+3+0+1 = 5
    # ones  = 1+1+1+0 = 3

    result = sol.findMaxForm(strs, m, n)
    print("Maximum number of strings:", result)

    # Example 2 (to show why forward iteration is wrong)
    strs2 = ["10"]
    m2 = 2
    n2 = 2

    # Correct answer = 1 (we can only use "10" once)
    # If we iterate FORWARD incorrectly, we might get 2 (wrong)

    result2 = sol.findMaxForm(strs2, m2, n2)
    print("Example 2 result:", result2)


# ---------------------- COMPLEXITY ----------------------
# Time Complexity: O(len(strs) * m * n)
# Space Complexity: O(m * n)

class Solution:

    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        # 1D DP array
        dp = [0] * n

        # Initialize first row
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]

        # Process remaining rows
        for i in range(1, m):
            # First column (can only come from top)
            dp[0] += grid[i][0]

            for j in range(1, n):
                # min(top, left) + current cell
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])

        return dp[-1]


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    sol = Solution()
    print("Minimum Path Sum:", sol.minPathSum(grid))


# ---------------- COMPLEXITY ----------------
# Time Complexity  : O(m * n)
# Space Complexity : O(n)
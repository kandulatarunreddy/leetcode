class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If start or end is blocked, no path exists
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # 1D DP array (space optimized)
        dp = [0] * n

        # Start position
        dp[0] = 1

        for i in range(m):
            for j in range(n):

                # If current cell is an obstacle → no paths through it
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0

                else:
                    # If not first column, add left cell contribution
                    if j > 0:
                        dp[j] += dp[j - 1]

        return dp[n - 1]


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    sol = Solution()
    print("Unique Paths II:", sol.uniquePathsWithObstacles(grid))


# ---------------- COMPLEXITY ----------------
# Time Complexity  : O(m * n)
# Space Complexity : O(n)
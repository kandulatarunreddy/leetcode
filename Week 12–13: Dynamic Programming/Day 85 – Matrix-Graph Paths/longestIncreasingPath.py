from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Dimensions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Memoization: (row, col) -> longest increasing path starting from here
        dp = {}

        def dfs(r, c, prevVal):
            """
            Returns the length of the longest increasing path
            starting from cell (r, c)

            prevVal = value of previous cell in the path
            """

            # ❌ Invalid cases:
            # 1. Out of bounds
            # 2. Not increasing (current value <= previous value)
            if (r < 0 or r >= ROWS or
                    c < 0 or c >= COLS or
                    matrix[r][c] <= prevVal):
                return 0

            # ✅ If already computed, return cached result
            if (r, c) in dp:
                return dp[(r, c)]

            """
            Start with length = 1 (the current cell itself)

            Example:
            matrix = [
              [9, 9, 4],
              [6, 6, 8],
              [2, 1, 1]
            ]

            If we're at value 4:
            path could be 4 → 8 → ... so we explore neighbors
            """
            res = 1

            # Explore all 4 directions
            # Down
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))

            # Up
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))

            # Right
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))

            # Left
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            # Save result in dp
            dp[(r, c)] = res

            return res

        # Run DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)  # -1 ensures first move is always valid

        # The answer is the maximum path found
        return max(dp.values())


# ✅ Test it (for IDEA / PyCharm)
if __name__ == "__main__":
    sol = Solution()

    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]

    print("Matrix:")
    for row in matrix:
        print(row)

    print("Longest Increasing Path:", sol.longestIncreasingPath(matrix))
#TC, SC: O(m∗n)
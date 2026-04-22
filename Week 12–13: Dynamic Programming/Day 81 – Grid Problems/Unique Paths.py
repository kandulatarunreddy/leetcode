class UniquePaths:

    # ---------------------------------------------------
    # 1. Recursion (Brute Force)
    # ---------------------------------------------------
    def unique_paths_recursive(self, m, n):
        # Base case: if we reach last row or last column
        if m == 1 or n == 1:
            return 1

        # Move down + move right
        return self.unique_paths_recursive(m - 1, n) + \
            self.unique_paths_recursive(m, n - 1)


    # ---------------------------------------------------
    # 2. Recursion + Memoization (Top-Down DP)
    # ---------------------------------------------------
    def unique_paths_memo(self, m, n):
        memo = {}

        def helper(i, j):
            if i == 1 or j == 1:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = helper(i - 1, j) + helper(i, j - 1)
            return memo[(i, j)]

        return helper(m, n)


    # ---------------------------------------------------
    # 3. Dynamic Programming (2D Table)
    # ---------------------------------------------------
    def unique_paths_dp(self, m, n):
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


    # ---------------------------------------------------
    # 4. Space Optimized DP (1D)
    # ---------------------------------------------------
    def unique_paths_optimized(self, m, n):
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]

        return dp[-1]


    # ---------------------------------------------------
    # 5. Combinatorics (Best Approach)
    # ---------------------------------------------------
    def unique_paths_math(self, m, n):
        """
        We need to go from top-left to bottom-right.

        Total moves required = (m-1) downs + (n-1) rights
                             = m + n - 2

        We must choose where to place the downs (or rights).
        So the answer is:
            C(m+n-2, m-1)  OR  C(m+n-2, n-1)

        Instead of using factorial:
            C(N, r) = N! / (r! * (N-r)!)

        We compute it iteratively to avoid large numbers:
            C(N, r) =
            (N-r+1)/1 × (N-r+2)/2 × ... × N/r
        """
        """
        Example Walkthrough:
        m = 3, n = 3
        
        Total steps = 3 + 3 - 2 = 4
        We choose 2 positions for "down" moves
        
        C(4,2) =
        (4-2+1)/1 × (4-2+2)/2
        = 3/1 × 4/2
        = 3 × 2
        = 6
        
        So output = 6
        """

        N = m + n - 2          # total steps
        r = min(m - 1, n - 1)  # choose smaller for efficiency

        result = 1

        # Build the combination step by step
        for i in range(1, r + 1):
            # Multiply by next numerator term and divide by i
            # This represents:
            # result *= (N-r+i)/i
            result = result * (N - r + i) // i

        return result


# ---------------------------------------------------
# Driver Code
# ---------------------------------------------------
if __name__ == "__main__":
    m, n = 3, 3
    solver = UniquePaths()

    print("Recursion:", solver.unique_paths_recursive(m, n))
    print("Memoization:", solver.unique_paths_memo(m, n))
    print("DP (2D):", solver.unique_paths_dp(m, n))
    print("DP (1D Optimized):", solver.unique_paths_optimized(m, n))
    print("Combinatorics:", solver.unique_paths_math(m, n))


"""
Example:
m = 3, n = 3

Grid paths:
Total = 6
"""

# ---------------------------------------------------
# Complexity Summary
# ---------------------------------------------------
# 1. Recursion:
#    TC = O(2^(m+n)), SC = O(m+n)  (stack)
#
# 2. Memoization:
#    TC = O(m*n), SC = O(m*n)
#
# 3. DP (2D):
#    TC = O(m*n), SC = O(m*n)
#
# 4. DP (1D):
#    TC = O(m*n), SC = O(n)
#
# 5. Combinatorics:
#    TC = O(min(m,n)), SC = O(1)
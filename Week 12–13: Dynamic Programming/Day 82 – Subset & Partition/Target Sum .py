def findTargetSumWays(nums, target):
    # Step 1: Calculate total sum
    total = sum(nums)

    # Step 2: Check if valid transformation is possible
    # We need: P = (total + target) // 2
    # Conditions:
    # - total + target must be even
    # - target should not exceed total
    if (total + target) % 2 != 0 or abs(target) > total:
        return 0

    subset_sum = (total + target) // 2

    # Step 3: DP array
    # dp[j] = number of ways to get sum j
    dp = [0] * (subset_sum + 1)

    # Base case: 1 way to make sum 0 (pick nothing)
    dp[0] = 1

    # Step 4: Fill DP
    for num in nums:
        # Go backward to avoid reusing same number
        for j in range(subset_sum, num - 1, -1):
            # If we TAKE num:
            # we add ways of forming (j - num)
            dp[j] += dp[j - num]

    return dp[subset_sum]


# -------------------------
# Driver code (run this)
# -------------------------
if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3

    result = findTargetSumWays(nums, target)
    print("Number of ways:", result)


# Time Complexity: O(n * subset_sum)
# Space Complexity: O(subset_sum)
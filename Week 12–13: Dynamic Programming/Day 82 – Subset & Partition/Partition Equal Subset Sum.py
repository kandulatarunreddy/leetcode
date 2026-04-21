def canPartition(nums):
    total = sum(nums)

    # If total sum is odd → cannot split equally
    if total % 2 != 0:
        return False

    target = total // 2

    # dp[j] = True if we can make sum j
    dp = [False] * (target + 1)

    # Base case
    dp[0] = True  # we can always make sum 0

    for num in nums:
        # Go backward (0/1 knapsack)
        for j in range(target, num - 1, -1):
            # Either we already could make j
            # OR we can make (j - num) and take num
            dp[j] = dp[j] or dp[j - num]

    return dp[target]


# -------------------------
# Driver code
# -------------------------
if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print("Can partition:", canPartition(nums))


# Time Complexity: O(n * target)
# Space Complexity: O(target)
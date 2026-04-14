from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add boundaries to avoid edge checks
        # Example: [3,1,5,8] → [1,3,1,5,8,1]
        nums = [1] + nums + [1]

        dp = {}  # memoization

        def dfs(l, r):
            """
            Solve subproblem for nums[l...r] (inclusive)

            IMPORTANT IDEA:
            We assume ALL balloons in (l, r) will be burst,
            and we try picking ONE balloon 'i' to be the LAST burst.

            So:
            - left side (l → i-1) is already gone
            - right side (i+1 → r) is already gone
            - ONLY balloon i remains at the end
            """

            # No balloons left
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0

            # Try each balloon as the LAST one to burst
            for i in range(l, r + 1):

                """
                Suppose:
                nums = [1,3,1,5,8,1]
                dfs(1,4) → working on [3,1,5,8]

                Pick i = 2 (value = 1)

                Step 1:
                Solve left → dfs(1,1) → [3]
                Solve right → dfs(3,4) → [5,8]

                Step 2:
                After left & right are BURST,
                ONLY nums[i] remains in this interval

                So the array effectively becomes:
                [1, _, 1, _, _, 1]

                Now balloon i is between:
                left boundary = nums[l-1]
                right boundary = nums[r+1]
                """

                # Coins from bursting i LAST
                # NOT nums[i-1] or nums[i+1] because those are already burst!
                coins = nums[l - 1] * nums[i] * nums[r + 1]

                # Add coins from subproblems
                coins += dfs(l, i - 1)   # burst left side first
                coins += dfs(i + 1, r)   # burst right side first

                # Take best choice
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        # Solve full problem (ignore the added 1s)
        return dfs(1, len(nums) - 2)


# ✅ Test it (this is what you need in IDEA)
if __name__ == "__main__":
    sol = Solution()

    nums = [3, 1, 5, 8]
    result = sol.maxCoins(nums)

    print("Input:", nums)
    print("Max Coins:", result)
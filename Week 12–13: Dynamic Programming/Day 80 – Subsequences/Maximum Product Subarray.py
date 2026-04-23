class Solution(object):
    def maxProduct(self, nums):
        minp = maxp = nums[0]
        maxprod = nums[0]

        for i in range(1, len(nums)):
            temp = minp
            minp = min(nums[i], minp * nums[i], maxp * nums[i])
            maxp = max(nums[i], temp * nums[i], maxp * nums[i])
            maxprod = max(maxprod, maxp)

        return maxprod

if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    sol = Solution()
    result = sol.maxProduct(nums)
    print("Maximum Product Subarray:", result)

#Time O(n), Space O(1)

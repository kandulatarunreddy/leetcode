from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        l = 0
        count = 0
        for r in range(len(nums)):
            prod *= nums[r]
            while prod >= k:
                prod //= nums[l]
                l += 1
            count += (r - l) + 1
        return count

sol=Solution()
nums = [3,4,-1,1]
print(sol.numSubarrayProductLessThanK(nums))
#tc:O(n), sc:O(1)
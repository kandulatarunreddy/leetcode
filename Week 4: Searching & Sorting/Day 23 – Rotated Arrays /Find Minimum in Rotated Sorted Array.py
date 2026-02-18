from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # If mid value is greater than right value,
            # the minimum must be in the right half
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # Minimum is in left half including mid
                r = mid
        return nums[l]
sol = Solution()
nums = [3,4,5,1,2]
print(sol.findMin(nums))
#Tc: O(logn) sc:O(1)
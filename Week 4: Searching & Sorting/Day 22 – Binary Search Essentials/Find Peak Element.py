from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                # Peak is on the right side
                l = mid + 1
            else:
                # Peak is on the left side or mid
                r = mid
        return l  # or r, they are equal at the end

# Example
sol = Solution()
nums = [1,2,1,3,5,6,4]
print(sol.findPeakElement(nums))  # Output: 1 or 5 (both peaks)
#Tc: O(logn) Sc: O(1)



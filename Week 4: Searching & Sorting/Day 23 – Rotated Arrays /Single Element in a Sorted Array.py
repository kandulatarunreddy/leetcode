from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Binary search boundaries
        l, r = 0, len(nums) - 1
        # Continue until search space reduces to one element
        while l < r:
            # Find middle index
            mid = l + (r - l) // 2
            # IMPORTANT:
            # We always want mid to point to the FIRST index of a pair.
            # Valid pairs start at EVEN indices (0,2,4,...).
            # If mid is odd, move one step left to make it even.
            if mid % 2 == 1:
                mid -= 1
            # Now compare the pair starting at mid:
            # Case 1: Pair is valid → single element is on the RIGHT side
            if nums[mid] == nums[mid + 1]:
                # Skip this valid pair completely
                l = mid + 2
            # Case 2: Pair is broken → single element is at mid or LEFT side
            else:
                r = mid
        # When l == r, we found the single element
        return nums[l]
sol = Solution()
nums = [1,1,2,3,3,4,4,8,8]
print(sol.singleNonDuplicate(nums))
#Tc: O(logn) sc:O(1)

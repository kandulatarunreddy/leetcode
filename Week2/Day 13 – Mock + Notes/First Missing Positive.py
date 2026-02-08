'''
Although there is a nested while loop, each element is swapped at most once into its correct position,
so the total number of swaps is O(n).
Therefore the overall time complexity is O(n) with O(1) extra space.'''
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            # place numbers in correct positions
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]

        # find first missing index
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

sol=Solution()
nums = [3,4,-1,1]
print(sol.firstMissingPositive(nums))
#tc:O(n), sc:O(1)


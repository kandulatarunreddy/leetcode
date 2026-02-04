from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                max_count = max(max_count, current)
            else:
                current = 0

        return max_count

nums = [1,1,0,1,1,1]
sol = Solution()
print(sol.findMaxConsecutiveOnes(nums))

#Time: O(n), Space: O(1)


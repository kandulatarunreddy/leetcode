from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = missing = 0
        # Mark seen numbers
        for num in nums:
            index = abs(num) - 1 #[2,2] gives why abs is required( [2,-2] )
            if nums[index] < 0:
                duplicate = abs(num)
            else:
                nums[index] *= -1

        # Find the missing number
        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1

        return [duplicate, missing]

sol = Solution()
print(sol.findErrorNums([1, 2, 2, 4]))
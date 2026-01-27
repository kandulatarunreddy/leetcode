from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # stores number -> index

        for i, num in enumerate(nums):
            if (target - num) in prevMap:
                return [prevMap[target - num], i]
            prevMap[num] = i
        return []

if __name__ == "__main__":
    solution = Solution()

    nums = [3, 2, 4]
    target = 6

    print("Input:", nums)
    print("Indices of numbers that sum to target:", solution.twoSum(nums, target))

#TC:O(n) , SC=O(n)
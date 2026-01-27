from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return False
            else:
                seen.add(num)
        return True
       
if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 1]   
    result = solution.containsDuplicate(nums)

    print("Input:", nums)
    print("Contains Duplicate:", result)

#TC:O(n) , SC=O(n)
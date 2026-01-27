from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        totalsum=sum(nums)
        for i,n in enumerate(nums):
            if leftsum==totalsum-leftsum-n:
                return i
            leftsum+=n
        return -1



if __name__ == "__main__":
    solution = Solution()

    nums = [1,2,3]

    print("Input:", nums)
    print("Indices of Pivot:", solution.pivotIndex(nums))

#TC:O(n) , SC=O(1)
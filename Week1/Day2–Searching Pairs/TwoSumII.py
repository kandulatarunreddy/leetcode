from typing import List 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                l+=1   

if __name__ == "__main__":
    solution = Solution()

    nums = [2,7,11,15]
    target = 9

    print("Input:", nums)
    print("Indices of numbers that sum to target:", solution.twoSum(nums, target))
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane’s Algorithm
        cursum=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            cursum=max(nums[i],cursum+nums[i])
            maxsum=max(cursum,maxsum)
        return maxsum


if __name__=="__main__":
    solution=Solution()
    nums = [5,4,-1,7,8]

    print("Input:", nums)
    print("maxSubArray:", solution.maxSubArray(nums))

#TC: O(n), SC: O(1)
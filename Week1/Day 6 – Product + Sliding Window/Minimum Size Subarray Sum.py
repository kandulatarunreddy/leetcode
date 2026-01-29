from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen=float("inf")
        l=0
        cursum=0
        for r in range(len(nums)):
            cursum+=nums[r]
            while cursum>=target:
                minlen=min(minlen,r-l+1)
                cursum-=nums[l]
                l+=1
        return minlen if minlen!=float("inf") else 0

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    sol = Solution()
    result = sol.minSubArrayLen(target,nums)
    print("minSubArrayLen :", result)

#Time O(n), Space O(1)
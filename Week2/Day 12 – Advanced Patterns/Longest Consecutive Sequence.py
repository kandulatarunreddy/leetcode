from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxlength=0
        for num in numset:
            if num-1 not in numset:
                count=1
                while num+count in numset:
                    count+=1
                maxlength=max(maxlength,count)
        return maxlength
sol=Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))
#tc:O(n), sc:O(n)

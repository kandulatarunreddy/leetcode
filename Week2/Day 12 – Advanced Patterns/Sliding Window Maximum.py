from typing import List, Deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=Deque()
        l,r=0,0
        output=[]
        while r<len(nums):
            #before appending check if any values is smaller in queue if so pop it out
            while q and nums[r]>nums[q[-1]]:
                q.pop()
            q.append(r)
            # check if left is out of bound [8,7,6,9], l=1, q[0]=0 means we're at 2 window of size k so pop left
            if l>q[0]:
                q.popleft()
            # check if we reach k size
            if r+1>=k:
                output.append(nums[q[0]])
                #increase left only after updatinig the output res.
                l+=1
            r+=1
        return output

nums = [1,2,1,0,4,2,6]
k = 3
sol = Solution()
print(sol.maxSlidingWindow(nums,k))

#Time: O(n), Space: O(1)

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            #skip the first element for duplicate in triplet.
            if i>0 and nums[i-1]==nums[i]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]>0:
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    #skip the second element for duplicate in triplet.
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

if __name__ == "__main__":
    solution = Solution()

    nums = [-1,0,1,2,-1,-4]

    print("Input:", nums)
    print("threeSum:", solution.threeSum(nums))

#TC: O(n^2) and sc=O(1)
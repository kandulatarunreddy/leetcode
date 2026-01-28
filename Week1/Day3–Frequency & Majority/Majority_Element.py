from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''Moore Voting Algorithm'''
        count=0
        candidate=0
        for num in nums:
            if count==0:
                candidate=num
            if num!=candidate:
                count-=1
            else:
                count+=1
        return candidate



if __name__ == "__main__":
    solution = Solution()

    nums = [1,1,2,2,3,2]

    print("Input:", nums)
    print("majorityElement:", solution.majorityElement(nums))

#TC: O(n), SC: O(1)
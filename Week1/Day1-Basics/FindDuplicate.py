class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        #Floyd’s Tortoise and Hare (Cycle Detection)
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow

if __name__ == "__main__":
    solution = Solution()

    nums = [3,1,3,4,2]
    result = solution.findDuplicate(nums)

    print("Input:", nums)
    print("Duplicate value:", result)

#TC: O(n), SC:O(1)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k


if __name__ == "__main__":
    solution = Solution()

    nums = [0,0,1,1,1,2,2,3,3,4] 
    result = solution.removeDuplicates(nums)

    print("Input:", nums)
    print("size after removeDuplicates:", result)

#TC: O(n), SC:O(1)
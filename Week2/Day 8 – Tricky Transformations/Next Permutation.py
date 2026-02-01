from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2

        # Step 1: Find first decreasing element from the end
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If such element exists, find element to swap with
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the subarray after index i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3]
    print("Original:", nums)
    solution.nextPermutation(nums)
    print("Next Permutation:", nums)
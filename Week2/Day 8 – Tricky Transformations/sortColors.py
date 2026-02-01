from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts nums in-place such that 0s, 1s, and 2s are grouped together.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swap 0 to the 'low' region
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is in the correct place, move on
                mid += 1
            else:  # nums[mid] == 2
                # Swap 2 to the 'high' region
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Don't increment mid here, because swapped element needs checking
if __name__ == "__main__":
    solution = Solution()

    nums = [2,0,2,1,1,0]
    print("Original:", nums)
    solution.sortColors(nums)
    print("sortColors:", nums)
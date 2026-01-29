from sys import prefix
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixsum = 0
        # HashMap to store how many times a prefix sum has occurred
        # {prefix_sum: frequency}
        # Initialize with 0 sum occurring once (important for subarrays starting at index 0)
        hashmap = {0: 1}

        for n in nums:
            # Add current element to running prefix sum
            prefixsum += n
            # If (prefixsum - k) exists in hashmap,
            # it means there are subarrays ending here whose sum = k
            if (prefixsum - k) in hashmap:
                count += hashmap[prefixsum - k]
            # Store/update the frequency of current prefix sum
            hashmap[prefixsum] = hashmap.get(prefixsum, 0) + 1

        # Return total count of subarrays
        return count


if __name__ == "__main__":
    solution = Solution()

    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7
    print("Input:", nums)
    print("subarraySum:", solution.subarraySum(nums,k))
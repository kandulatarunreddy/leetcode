from typing import List
class Solution:
    def subarrayXor(self, nums: List[int], k: int) -> int:
        count = 0
        prefixXor = 0

        # HashMap to store frequency of prefix XORs
        hashmap = {0: 1}  # XOR 0 occurs once initially

        for n in nums:
            # Update running XOR
            prefixXor ^= n

            # If (prefixXor ^ k) exists,
            # it means there are subarrays ending here with XOR = k
            if (prefixXor ^ k) in hashmap:
                count += hashmap[prefixXor ^ k]

            # Store/update frequency of current prefix XOR
            hashmap[prefixXor] = hashmap.get(prefixXor, 0) + 1

        return count

if __name__ == "__main__":
    solution = Solution()

    nums = [5, 6, 7, 8, 9]
    k = 5
    print("Input:", nums)
    print("subarrayXor:", solution.subarrayXor(nums,k))
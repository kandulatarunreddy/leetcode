from typing import List

def canJump(nums: List[int]) -> bool:
    """
    Determines if you can reach the last index of the array.

    Approach: Greedy
    - Keep track of the farthest index we can reach so far.
    - If at any index, we cannot reach it (i > farthest), return False.
    - Otherwise, update farthest with max(farthest, i + nums[i]).
    """
    farthest = 0  # farthest index we can reach initially

    for i, jump in enumerate(nums):
        # if current index is beyond reachable range, return False
        if i > farthest:
            return False

        # update farthest reachable index from current position
        farthest = max(farthest, i + jump)

    # if we can reach or go beyond the last index, return True
    return True


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([2,3,1,1,4], True),   # Can reach end
        ([3,2,1,0,4], False),  # Stuck at index 3
        ([0], True),           # Already at last index
        ([2,0,0], True),       # Jump over zeros
        ([1,0,2], False)       # Cannot jump over zero
    ]

    for nums, expected in test_cases:
        result = canJump(nums)
        print(f"Input: {nums} -> Can jump? {result} (Expected: {expected})")


# Time Complexity: O(n), because we traverse the array once
# Space Complexity: O(1), only using a single variable 'farthest'
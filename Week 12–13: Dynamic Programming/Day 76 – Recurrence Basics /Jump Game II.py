def jump(nums):
    """
    Find the minimum number of jumps to reach the last index.

    Args:
    nums (List[int]): List of non-negative integers where nums[i] is max jump length from index i.

    Returns:
    int: Minimum number of jumps to reach last index.
    """

    n = len(nums)
    if n <= 1:
        return 0  # Already at the last index, no jumps needed

    jumps = 0        # Counts the number of jumps made
    current_end = 0  # Farthest we can reach with current number of jumps
    farthest = 0     # Farthest we can reach while scanning current jump range

    # Loop through all indices except the last one
    for i in range(n - 1):
        # Update farthest reachable index from current index
        farthest = max(farthest, i + nums[i])

        # If we have reached the end of the current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest  # Move the current jump range to the farthest reachable

            # Optional: early exit if we can already reach or exceed the last index
            if current_end >= n - 1:
                break

    return jumps

'''
def jump(self, nums: List[int]) -> int:
        current_end=0
        jumps=0
        farthest=0
        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])

            if i==current_end:
                jumps+=1
                current_end=farthest
        return jumps
'''

# Example usage:
nums = [2,3,1,1,4]
print(jump(nums))  # Output: 2

nums2 = [1,1,1,1,1]
print(jump(nums2))  # Output: 4

nums3 = [6,2,4,0,5,1,1,4,2,9]
print(jump(nums3))  # Output: 2

# Time Complexity: O(n), we scan each element once
# Space Complexity: O(1), constant extra space used


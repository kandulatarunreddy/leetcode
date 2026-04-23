import bisect

def length_of_lis(nums):
    """
    Returns the length of the Longest Increasing Subsequence (LIS)
    using an O(n log n) approach.
    """

    # tails[i] will be the smallest possible tail
    # of an increasing subsequence of length i+1
    tails = []

    for num in nums:
        # Find the position where 'num' should go
        # in the sorted 'tails' list
        idx = bisect.bisect_left(tails, num)

        # If num is larger than all elements in tails,
        # it extends the longest subsequence
        if idx == len(tails):
            tails.append(num)
        else:
            # Otherwise, replace the existing value
            # to maintain the smallest possible tail
            tails[idx] = num

    # The length of tails is the length of LIS
    return len(tails)


# Example usage
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(length_of_lis(nums))  # Output: 4

#Time Complexity: O(n log n)
#Space Complexity: O(n)
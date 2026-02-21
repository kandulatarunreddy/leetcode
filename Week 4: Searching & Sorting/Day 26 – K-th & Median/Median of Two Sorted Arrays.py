from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ------------------------------------------------------------
        # We will use binary search on the smaller array.
        # This guarantees O(log(min(m, n))) time complexity.
        # ------------------------------------------------------------

        A, B = nums1, nums2
        total = len(A) + len(B)     # Total number of elements
        half = total // 2           # Size of left partition

        # Ensure A is the smaller array.
        # This keeps binary search efficient and prevents index errors.
        if len(B) < len(A):
            A, B = B, A

        # Binary search boundaries on A
        # We search over indices of A's left partition end.
        l, r = 0, len(A) - 1

        # We use an infinite loop because we are guaranteed
        # to find a valid partition (problem constraints ensure this).
        while True:

            # --------------------------------------------------------
            # i = index of last element in A's left partition
            # j = index of last element in B's left partition
            #
            # Why j = half - i - 2 ?
            #
            # If A's left partition has (i + 1) elements
            # and B's left partition has (j + 1) elements,
            #
            # Then:
            # (i + 1) + (j + 1) = half
            #
            # Solve:
            # i + j + 2 = half
            # j = half - i - 2
            # --------------------------------------------------------
            i = (l + r) // 2
            j = half - i - 2

            # --------------------------------------------------------
            # Now we identify the four boundary values:
            #
            # Aleft  = largest value on left side of A
            # Aright = smallest value on right side of A
            # Bleft  = largest value on left side of B
            # Bright = smallest value on right side of B
            #
            # We use +/- infinity to handle edge cases
            # when partition is at extreme ends.
            # --------------------------------------------------------

            Aleft  = A[i]     if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")

            Bleft  = B[j]     if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # --------------------------------------------------------
            # Check if we found the correct partition.
            #
            # The partition is valid if:
            # max(left side) <= min(right side)
            #
            # Which translates to:
            # Aleft <= Bright AND Bleft <= Aright
            # --------------------------------------------------------
            if Aleft <= Bright and Bleft <= Aright:

                # ----------------------------------------------------
                # If total number of elements is odd:
                # Median is the first element of the right partition.
                # ----------------------------------------------------
                if total % 2:
                    return min(Aright, Bright)

                # ----------------------------------------------------
                # If total number of elements is even:
                # Median is average of:
                #   max(left partition) and min(right partition)
                # ----------------------------------------------------
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # --------------------------------------------------------
            # If partition is incorrect, adjust binary search:
            #
            # Case 1:
            # Aleft > Bright
            # → We are too far right in A
            # → Move left
            #
            # Case 2:
            # Bleft > Aright
            # → We are too far left in A
            # → Move right
            # --------------------------------------------------------
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
# =========================
# Run / Test the Solution
# =========================
if __name__ == "__main__":
    solution = Solution()

    # Example 1 (Odd total length)
    nums1 = [1, 3]
    nums2 = [2]
    print("Median:", solution.findMedianSortedArrays(nums1, nums2))  # Expected: 2

    # Example 2 (Even total length)
    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Median:", solution.findMedianSortedArrays(nums1, nums2))  # Expected: 2.5

    # Additional test
    nums1 = [1, 5, 8]
    nums2 = [2, 3, 7, 9]
    print("Median:", solution.findMedianSortedArrays(nums1, nums2))
"""
    Finds the median of two sorted arrays using binary search.

    Time Complexity: O(log(min(m, n)))
        - We binary search only on the smaller array.

    Space Complexity: O(1)
        - We use only a few variables (constant extra space).
    """

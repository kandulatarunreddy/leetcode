from typing import List


class Solution:
    """
    Finds the K-th smallest element in two sorted arrays
    using binary search partition method.

    Time Complexity: O(log(min(m, n)))
        - We binary search only on the smaller array.

    Space Complexity: O(1)
        - Only constant extra variables are used.
    """

    def findKthElement(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # ------------------------------------------------------------
        # We will use binary search on the smaller array.
        # This guarantees O(log(min(m, n))) time complexity.
        # ------------------------------------------------------------

        A, B = nums1, nums2

        # Ensure A is the smaller array.
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)

        # ------------------------------------------------------------
        # We choose:
        #   i = number of elements taken from A
        #   j = number of elements taken from B
        #
        # Such that:
        #   i + j = k
        #
        # Since:
        #   j = k - i
        #
        # We must ensure:
        #   0 ≤ i ≤ m
        #   0 ≤ j ≤ n
        #
        # From:
        #   0 ≤ k - i ≤ n
        #
        # We derive:
        #   k - n ≤ i ≤ k
        #
        # Combining with:
        #   0 ≤ i ≤ m
        #
        # Final valid search range:
        #   max(0, k - n) ≤ i ≤ min(k, m)
        # ------------------------------------------------------------

        left = max(0, k - n)
        right = min(k, m)

        while left <= right:

            # Number of elements taken from A
            i = (left + right) // 2

            # Number of elements taken from B
            j = k - i


            Aleft  = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")

            Bleft  = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            # --------------------------------------------------------
            # Valid partition condition:
            #
            # max(left side) <= min(right side)
            #
            # Aleft <= Bright AND Bleft <= Aright
            # --------------------------------------------------------
            if Aleft <= Bright and Bleft <= Aright:

                # If valid partition found,
                # K-th smallest element is the largest in left partition
                return max(Aleft, Bleft)

            # If Aleft too big, move left
            elif Aleft > Bright:
                right = i - 1

            # Else move right
            else:
                left = i + 1

        return -1  # Should never happen if inputs are valid


# =========================
# Run / Test the Solution
# =========================
if __name__ == "__main__":
    solution = Solution()

    nums1 = [2, 3, 6, 7, 9]
    nums2 = [1, 4, 8, 10]

    k = 5
    print("K-th Element:", solution.findKthElement(nums1, nums2, k))
    # Expected Output: 6

    k = 1
    print("K-th Element:", solution.findKthElement(nums1, nums2, k))
    # Expected Output: 1

    k = 9
    print("K-th Element:", solution.findKthElement(nums1, nums2, k))
    # Expected Output: 10
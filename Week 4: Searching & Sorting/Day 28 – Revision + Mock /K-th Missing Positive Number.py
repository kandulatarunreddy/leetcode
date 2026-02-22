class Solution:
    def findKthPositive(self, arr, k):
        """
        Returns the k-th missing positive number
        from a sorted strictly increasing array.
        """

        # Binary search range
        low = 0
        high = len(arr) - 1

        # We search for the first index
        # where missing numbers >= k
        while low <= high:

            mid = (low + high) // 2

            # -----------------------------------------
            # Calculate how many numbers are missing
            # up to index 'mid'
            #
            # Formula:
            # missing = arr[mid] - (mid + 1)
            #
            # Why?
            # If no numbers were missing:
            # arr[mid] should equal mid+1
            #
            # So difference gives missing count.
            # -----------------------------------------
            missing = arr[mid] - (mid + 1)

            if missing < k:
                # We still need more missing numbers
                # So move right
                low = mid + 1
            else:
                # Too many missing numbers
                # Move left to find smaller index
                high = mid - 1

        # After loop ends:
        # 'low' is the position where
        # k-th missing number belongs.

        # The k-th missing number is:
        #
        # low + k
        #
        # This formula works because:
        # low elements exist before it,
        # and we need to shift by k.
        return low + k


# -------------------------
# Example Run
# -------------------------
if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    k = 5

    obj = Solution()
    print("K-th Missing Number:", obj.findKthPositive(arr, k))


# Time Complexity: O(log n)
# Space Complexity: O(1)
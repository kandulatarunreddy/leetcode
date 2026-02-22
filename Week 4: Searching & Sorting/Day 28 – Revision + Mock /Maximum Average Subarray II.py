class Solution:
    def findMaxAverage(self, nums, k):
        """
        PROBLEM:
        Find maximum average of any subarray with length >= k.

        APPROACH:
        1. Binary Search on possible average (mid)
        2. For each mid, check if such average is possible.
        3. Convert average problem into subarray sum problem.
        """

        # -------------------------------------------------------
        # WHY TRANSFORM THE ARRAY?
        # -------------------------------------------------------
        # We want to check:
        #
        #     average >= mid
        #
        # This means:
        #
        #     sum / length >= mid
        #
        # Multiply both sides:
        #
        #     sum >= mid * length
        #
        # Rearranged:
        #
        #     sum - mid * length >= 0
        #
        # Instead of checking average directly,
        # we transform each element:
        #
        #     new_value = nums[i] - mid
        #
        # Why?
        #
        # Because:
        # If we sum these new values,
        # it becomes:
        #
        #     (original sum) - mid * length
        #
        # Exactly what we need!
        # -------------------------------------------------------

        def can_find(mid):

            n = len(nums)

            # Prefix sum of transformed array
            # prefix[i] = sum of nums[0:i] after subtracting mid
            #
            # Example:
            # nums = [5, 6]
            # mid = 4
            #
            # transformed = [1, 2]
            # prefix = [0, 1, 3]
            #
            # prefix[0] = 0 (base case)
            # This helps calculate subarray sums easily.
            prefix = [0] * (n + 1)

            for i in range(n):
                prefix[i + 1] = prefix[i] + (nums[i] - mid)

            # We must ensure subarray length >= k
            #
            # Suppose k = 2
            #
            # For subarray ending at index i,
            # starting index must be <= i - k
            #
            # That is why we only start checking from i = k
            # -------------------------------------------------------

            min_prefix = 0  # smallest prefix seen so far

            for i in range(k, n + 1):

                # ---------------------------------------------------
                # Why check:
                #
                #     prefix[i] - min_prefix >= 0 ?
                #
                # Because:
                #
                # Subarray sum = prefix[i] - prefix[j]
                #
                # We want:
                #
                #     prefix[i] - prefix[j] >= 0
                #
                # To maximize chances,
                # we use the smallest prefix value seen so far.
                #
                # Example:
                #
                # prefix values: [0, -1, 2, -3]
                #
                # Smallest so far = -3
                #
                # That gives best chance for:
                # prefix[i] - min_prefix
                # ---------------------------------------------------

                if prefix[i] - min_prefix >= 0:
                    return True

                # ---------------------------------------------------
                # Why update min_prefix like this?
                #
                # We must maintain subarray length >= k.
                #
                # For subarray ending at i,
                # valid starting positions are:
                #
                #     j <= i - k
                #
                # So we only allow prefix values
                # up to index (i - k).
                #
                # That is why we use:
                #
                #     prefix[i - k + 1]
                #
                # Example:
                #
                # If k = 2
                # and i = 3
                #
                # Then valid j <= 1
                #
                # So we update using prefix[2]
                # ---------------------------------------------------

                min_prefix = min(min_prefix, prefix[i - k + 1])

            return False

        # -------------------------------------------------------
        # Binary Search on Average
        # -------------------------------------------------------

        # Minimum possible average
        low = min(nums)

        # Maximum possible average
        high = max(nums)

        # Precision for floating point
        precision = 1e-5

        # Continue until range is small enough
        while high - low > precision:

            mid = (low + high) / 2.0

            if can_find(mid):
                # If mid is possible,
                # try larger average
                low = mid
            else:
                # Otherwise try smaller average
                high = mid

        return low


# -------------------------------------------------------
# Time Complexity:
# O(n * log(range))
# where range = max(nums) - min(nums)

# Space Complexity:
# O(n) due to prefix array
# -------------------------------------------------------
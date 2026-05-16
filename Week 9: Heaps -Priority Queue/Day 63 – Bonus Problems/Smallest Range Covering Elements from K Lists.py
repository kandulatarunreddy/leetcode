import heapq


class Solution:
    def smallestRange(self, nums):

        # Min heap stores:
        # (value, list_index, element_index)
        min_heap = []

        # Track largest element among current choices
        current_max = float("-inf")

        # -----------------------------------------
        # Example:
        #
        # nums = [
        #     [1, 4],
        #     [2, 5],
        #     [3, 6]
        # ]
        #
        # Put first element from every list:
        #
        # heap = [1, 2, 3]
        # current_max = 3
        #
        # Current range = [1, 3]
        # -----------------------------------------
        for list_index, current_list in enumerate(nums):

            value = current_list[0]

            heapq.heappush(
                min_heap,
                (value, list_index, 0)
            )

            current_max = max(current_max, value)

        # Best range found so far
        best_start = float("-inf")
        best_end = float("inf")

        # Continue until one list finishes
        while True:

            # Get smallest value
            #
            # Example:
            # heap = [1, 2, 3]
            #
            # current_min = 1
            current_min, list_index, element_index = heapq.heappop(
                min_heap
            )

            # -----------------------------------------
            # Current valid range:
            #
            # [current_min, current_max]
            #
            # Example:
            #
            # [1, 3]
            #
            # because:
            # chosen values are 1,2,3
            # -----------------------------------------
            if (
                    current_max - current_min
                    < best_end - best_start
            ):
                best_start = current_min
                best_end = current_max

            # -----------------------------------------
            # Why move the minimum?
            #
            # Example:
            #
            # Current:
            # [1, 2, 3]
            #
            # Range = [1,3]
            #
            # To improve range,
            # increasing 2 or 3 won't help.
            #
            # Must increase smallest number (1).
            #
            # Move forward in same list:
            #
            # [4, 2, 3]
            #
            # New range = [2,4]
            # -----------------------------------------
            element_index += 1

            # -----------------------------------------
            # If this list ends,
            # impossible to pick one number
            # from every list anymore.
            #
            # Example:
            #
            # nums = [
            #   [1],
            #   [2,5],
            #   [3]
            # ]
            #
            # Once [1] finishes -> stop
            # -----------------------------------------
            if element_index == len(nums[list_index]):
                break

            # Get next number
            next_value = nums[list_index][element_index]

            # Add next element to heap
            #
            # Example:
            #
            # Before:
            # [1,2,3]
            #
            # Remove 1
            # Add 4
            #
            # New heap:
            # [2,3,4]
            heapq.heappush(
                min_heap,
                (
                    next_value,
                    list_index,
                    element_index
                )
            )

            # Update largest value
            #
            # Example:
            #
            # current_max = 3
            # next_value = 4
            #
            # new current_max = 4
            current_max = max(
                current_max,
                next_value
            )

        return [best_start, best_end]


# Example run in IntelliJ IDEA / PyCharm
nums = [
    [4, 10, 15, 24, 26],
    [0, 9, 12, 20],
    [5, 18, 22, 30]
]

sol = Solution()
print(sol.smallestRange(nums))

# Time Complexity: O(N log k)
# Space Complexity: O(k)
#
# N = total number of elements across all lists
# k = number of lists
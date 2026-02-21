from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on start time
        intervals.sort(key=lambda pair: pair[0])

        # Initialize output with first interval
        output = [intervals[0]]

        # Start from second interval (index 1)
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            # ------------------------------------------------
            # If overlapping:
            # Example: [1,5] and [2,4]
            # 2 <= 5 → Overlap
            # We merge by taking max end → max(5,4) = 5
            # ------------------------------------------------
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)

            # ------------------------------------------------
            # If no overlap:
            # Example: [1,5] and [7,8]
            # 7 > 5 → No overlap
            # Add new interval
            # ------------------------------------------------
            else:
                output.append([start, end])

        return output
if __name__ == "__main__":
    solution = Solution()

    intervals = [[1,3],[2,6],[8,10],[15,18]]

    print("res: ", solution.merge(intervals))

# -------------------------------------------------------
# Time Complexity (TC): O(n log n)
# Sorting dominates.
#
# Space Complexity (SC): O(n)
# Output list in worst case stores all intervals.
# -------------------------------------------------------
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # ---------------------------------------------------
        # 1️⃣ Condition: intervals[i][1] < newInterval[0]
        #
        # Meaning:
        # Current interval ends BEFORE newInterval starts.
        # Example:
        # [1,3] and newInterval = [5,7]
        # 3 < 5  → No overlap
        #
        # So we can safely add this interval to result.
        # ---------------------------------------------------
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # ---------------------------------------------------
        # 2️⃣ Condition: intervals[i][0] <= newInterval[1]
        #
        # Meaning:
        # Current interval starts BEFORE OR AT the time
        # newInterval ends.
        #
        # This means the intervals OVERLAP.
        #
        # Example:
        # intervals[i] = [1,3]
        # newInterval   = [2,5]
        #
        # Check:
        # 1 <= 5 → Overlap
        #
        # So we MERGE them by:
        # new start = min(starts)
        # new end   = max(ends)
        #
        # After merging:
        # [1,3] + [2,5] → [1,5]
        # ---------------------------------------------------
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval
        result.append(newInterval)

        # 3️⃣ Add remaining intervals (those completely after)
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

if __name__ == "__main__":
    solution = Solution()

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]

    k = 5
    print("res: ", solution.insert(intervals,newInterval))

# -------------------------------------------------------
# Time Complexity (TC): O(n)
# We traverse the intervals only once.
#
# Space Complexity (SC): O(1)
# Extra space is constant (excluding output list).
# -------------------------------------------------------
import heapq


class Solution:
    def minMeetingRooms(self, intervals):

        # Edge case:
        # No meetings -> no rooms needed
        if not intervals:
            return 0

        # -----------------------------------------
        # Sort meetings by start time
        #
        # Example:
        #
        # Before:
        # [[5,10], [0,30], [15,20]]
        #
        # After:
        # [[0,30], [5,10], [15,20]]
        # -----------------------------------------
        intervals.sort(key=lambda x: x[0])

        # Min heap stores meeting END TIMES
        #
        # Why?
        #
        # We want to quickly know:
        # Which room becomes free first?
        #
        min_heap = []

        # -----------------------------------------
        # Put first meeting's end time
        #
        # Example:
        #
        # meeting = [0,30]
        #
        # heap = [30]
        #
        # Means:
        # One room occupied until time 30
        # -----------------------------------------
        heapq.heappush(min_heap, intervals[0][1])

        # Process remaining meetings
        for start, end in intervals[1:]:

            # -----------------------------------------
            # Example:
            #
            # Current heap:
            # [10,30]
            #
            # start = 15
            #
            # Since 10 <= 15,
            # earliest room becomes free
            # -----------------------------------------
            if min_heap[0] <= start:

                # Reuse room
                heapq.heappop(min_heap)

            # -----------------------------------------
            # Add current meeting end time
            #
            # Example:
            #
            # Current meeting = [15,20]
            #
            # heap = [20,30]
            # -----------------------------------------
            heapq.heappush(min_heap, end)

        # Heap size = rooms needed
        return len(min_heap)


# Example run in IntelliJ IDEA / PyCharm
intervals = [[0, 30], [5, 10], [15, 20]]

sol = Solution()
print(sol.minMeetingRooms(intervals))

# Time Complexity: O(N log N)
# Space Complexity: O(N)
#
# N = number of meetings
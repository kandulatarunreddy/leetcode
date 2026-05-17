from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks, n):

        # -----------------------------------------
        # Count frequency of each task
        #
        # Example:
        #
        # tasks = [A,A,A,B,B,B]
        #
        # frequency:
        #
        # A -> 3
        # B -> 3
        # -----------------------------------------
        frequency = Counter(tasks)

        # -----------------------------------------
        # Max heap
        #
        # Python only supports min heap,
        # so we store negative counts
        #
        # Example:
        #
        # A -> 3
        # B -> 3
        #
        # heap:
        # [-3, -3]
        #
        # Most frequent task comes first
        # -----------------------------------------
        max_heap = []

        for count in frequency.values():
            heapq.heappush(max_heap, -count)

        # -----------------------------------------
        # Cooldown queue
        #
        # Stores:
        #
        # (available_time, remaining_count)
        #
        # Example:
        #
        # (3, -2)
        #
        # Means:
        #
        # At time = 3,
        # this task becomes reusable
        #
        # Still has 2 executions left
        #
        # We don't store A/B because
        # problem only asks minimum time,
        # not actual schedule.
        # -----------------------------------------
        cooldown = deque()

        # CPU current time
        time = 0

        # -----------------------------------------
        # Continue until:
        #
        # 1. No task left in heap
        # 2. No task cooling down
        # -----------------------------------------
        while max_heap or cooldown:

            # Move CPU time forward
            time += 1

            # -----------------------------------------
            # Execute most frequent available task
            #
            # Example:
            #
            # heap = [-3,-3]
            #
            # pop -> -3
            #
            # Suppose this is A
            # -----------------------------------------
            if max_heap:
                count = heapq.heappop(max_heap)

                # One execution completed
                #
                # Example:
                #
                # A had 3 remaining
                #
                # -3 -> -2
                #
                # Still 2 A's left
                count += 1

                # -----------------------------------------
                # If task still remains
                #
                # Put into cooldown
                #
                # Example:
                #
                # time = 1
                # n = 2
                #
                # A executed at time 1
                #
                # Cannot run again until:
                #
                # 1 + 2 = 3
                #
                # Add:
                #
                # (3, -2)
                #
                # Meaning:
                #
                # At time 3,
                # this task comes back
                # with 2 remaining.
                # -----------------------------------------
                if count < 0:
                    cooldown.append((time + n, count))

            # -----------------------------------------
            # Bring task back after cooldown
            #
            # Example:
            #
            # cooldown:
            # [(3,-2), (4,-2)]
            #
            # time = 3
            #
            # Bring back:
            # -2
            #
            # Meaning:
            # Task becomes reusable again
            # -----------------------------------------
            if cooldown and cooldown[0][0] == time:
                _, count = cooldown.popleft()
                heapq.heappush(max_heap, count)

        # Total intervals needed
        return time


# Example run in IntelliJ IDEA / PyCharm

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

sol = Solution()
print(sol.leastInterval(tasks, n))

# Time Complexity: O(N log K)
# Space Complexity: O(K)
#
# N = number of tasks
# K = number of unique tasks
import heapq


class Solution:
    def connectSticks(self, sticks):

        # Edge case:
        # 0 or 1 stick -> no cost needed
        if len(sticks) <= 1:
            return 0

        # -----------------------------------------
        # Convert list into min heap
        #
        # Example:
        #
        # sticks = [2,4,3]
        #
        # heap becomes:
        # [2,3,4]
        # -----------------------------------------
        heapq.heapify(sticks)

        # Store total cost
        total_cost = 0

        # Continue until only one stick remains
        while len(sticks) > 1:

            # -----------------------------------------
            # Pick 2 smallest sticks
            #
            # Example:
            #
            # heap = [2,3,4]
            #
            # first = 2
            # second = 3
            # -----------------------------------------
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)

            # Cost to connect them
            current_cost = first + second

            # Add to total answer
            total_cost += current_cost

            # -----------------------------------------
            # Push combined stick back
            #
            # Example:
            #
            # 2 + 3 = 5
            #
            # heap becomes:
            # [4,5]
            # -----------------------------------------
            heapq.heappush(sticks, current_cost)

        return total_cost


# Example run in IntelliJ IDEA / PyCharm
sticks = [2, 4, 3]

sol = Solution()
print(sol.connectSticks(sticks))

# Time Complexity: O(N log N)
# Space Complexity: O(N)
#
# N = number of sticks
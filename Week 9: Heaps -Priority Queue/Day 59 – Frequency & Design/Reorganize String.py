from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s):

        # Count frequency of each character
        #
        # Example:
        # "aaabbc"
        #
        # {
        #   'a': 3,
        #   'b': 2,
        #   'c': 1
        # }
        frequency = Counter(s)

        # -----------------------------------------
        # Impossible check
        #
        # If one character appears
        # more than ceil(n/2),
        # answer impossible
        #
        # Example:
        #
        # "aaab"
        #
        # a = 3
        # n = 4
        #
        # (4 + 1)//2 = 2
        #
        # 3 > 2 → impossible
        # -----------------------------------------
        max_allowed = (len(s) + 1) // 2

        for count in frequency.values():
            if count > max_allowed:
                return ""

        # -----------------------------------------
        # Max heap
        #
        # Python has min heap,
        # so use negative frequency
        #
        # Example:
        #
        # [(-3,'a'), (-2,'b'), (-1,'c')]
        # -----------------------------------------
        max_heap = []

        for char, count in frequency.items():
            heapq.heappush(max_heap,(-count, char))

        result = []

        # Store previous character
        #
        # Example:
        #
        # previous_count = -2
        # previous_char = 'a'
        #
        # Means:
        # still 2 'a' remaining
        previous_count = 0
        previous_char = ""

        while max_heap:

            # -----------------------------------------
            # Pick most frequent character
            #
            # Example:
            #
            # (-3,'a')
            # -----------------------------------------
            count, char = heapq.heappop(max_heap)

            # Add character to answer
            result.append(char)

            # One character used
            #
            # Example:
            #
            # -3 → -2
            count += 1

            # -----------------------------------------
            # Add previous character back
            #
            # Example:
            #
            # We previously used:
            # 'a'
            #
            # Now safe to reuse it
            # -----------------------------------------
            if previous_count < 0:
                heapq.heappush(max_heap,(previous_count,previous_char))

            # Save current character
            # for next iteration
            previous_count = count
            previous_char = char

        return "".join(result)


# Example run in IntelliJ IDEA / PyCharm
s = "aaabbc"

sol = Solution()
print(sol.reorganizeString(s))

# Time Complexity: O(N log K)
# Space Complexity: O(K)
#
# N = length of string
# K = unique characters
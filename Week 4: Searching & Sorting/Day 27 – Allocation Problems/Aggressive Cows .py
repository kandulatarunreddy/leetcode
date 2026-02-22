class Solution:
    def aggressiveCows(self, stalls, k):
        """
        Function to find the largest minimum distance between k cows
        placed in given stall positions.
        """

        # Step 1: Sort the stall positions
        # Sorting ensures we place cows in increasing order of position
        stalls.sort()

        # Helper function to check if we can place k cows
        # such that minimum distance between them is at least 'dist'
        def canPlace(dist):
            # Place first cow in the first stall
            count = 1
            last_position = stalls[0]

            # Try placing remaining cows
            for i in range(1, len(stalls)):

                # If current stall is at least 'dist' away
                # from last placed cow, place cow here
                if stalls[i] - last_position >= dist:
                    count += 1
                    last_position = stalls[i]

                # If we have placed all cows successfully
                if count >= k:
                    return True

            # Not possible to place all cows with this minimum distance
            return False

        # Step 2: Binary search on answer (minimum distance)
        low = 1  # minimum possible distance
        high = stalls[-1] - stalls[0]  # maximum possible distance
        answer = 0

        while low <= high:
            mid = (low + high) // 2  # candidate minimum distance

            # Check if we can place cows with 'mid' distance
            if canPlace(mid):
                answer = mid          # store valid answer
                low = mid + 1         # try for bigger minimum distance
            else:
                high = mid - 1        # try smaller distance

        return answer


# Example usage
if __name__ == "__main__":
    stalls = [1, 2, 4, 8, 9]
    k = 3
    obj = Solution()
    print(obj.aggressiveCows(stalls, k))  # Output: 3
'''	.    Sorting: O(n log n)
	•	Binary search: O(log(max_distance))
	•	Feasibility check per iteration: O(n)'''

# Time Complexity: O(n log n + n log(max_distance))
# Space Complexity: O(1)
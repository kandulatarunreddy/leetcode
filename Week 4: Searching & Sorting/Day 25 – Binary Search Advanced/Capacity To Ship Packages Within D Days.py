from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # --------------------------------------------------
        # 1️⃣ Define Binary Search Space
        # --------------------------------------------------

        # Minimum capacity must be at least the heaviest package
        left = max(weights)

        # Maximum capacity is shipping all packages in one day
        right = sum(weights)

        # --------------------------------------------------
        # 2️⃣ Binary Search for Minimum Valid Capacity
        # --------------------------------------------------

        while left < right:

            # Try middle capacity
            capacity = (left + right) // 2

            # --------------------------------------------------
            # 3️⃣ Check how many days are needed with this capacity
            # --------------------------------------------------

            needed_days = 1      # We start with Day 1
            current_load = 0     # Current day's total weight

            for w in weights:

                # If adding this package exceeds capacity,
                # we must move to the next day
                if current_load + w > capacity:
                    needed_days += 1      # Use one more day
                    current_load = 0      # Reset load for new day

                # Add package to current day's load
                current_load += w

            # --------------------------------------------------
            # 4️⃣ Adjust Search Space
            # --------------------------------------------------

            if needed_days <= days:
                # Capacity works — try smaller capacity
                right = capacity
            else:
                # Capacity too small — increase it
                left = capacity + 1

        # When left == right, this is the minimum valid capacity
        return left


# --------------------------------------------------
# Example Run (For Local IDE Execution)
# --------------------------------------------------
if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5

    sol = Solution()
    result = sol.shipWithinDays(weights, days)

    print("Minimum capacity required:", result)


# Time Complexity: O(n log S), S = sum(weights)
# Space Complexity: O(1)
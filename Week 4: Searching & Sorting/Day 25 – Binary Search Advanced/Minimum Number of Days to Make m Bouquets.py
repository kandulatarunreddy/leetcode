from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        # --------------------------------------------------
        # 1️⃣ If total flowers are less than m * k,
        #    it's impossible to form m bouquets.
        # --------------------------------------------------
        if m * k > len(bloomDay):
            return -1

        # --------------------------------------------------
        # 2️⃣ Binary search range:
        #    Minimum possible day = earliest bloom
        #    Maximum possible day = latest bloom
        # --------------------------------------------------
        left = min(bloomDay)
        right = max(bloomDay)

        # --------------------------------------------------
        # 3️⃣ Binary search to find minimum valid day
        # --------------------------------------------------
        while left < right:

            # Try middle day
            mid = (left + right) // 2

            # Count how many bouquets we can make by day = mid
            bouquets = 0          # number of bouquets formed
            consecutive = 0       # count of consecutive bloomed flowers

            for day in bloomDay:

                # --------------------------------------------------
                # If bloomDay[i] <= mid:
                # It means this flower has bloomed ON or BEFORE day mid.
                # So it is usable.
                # --------------------------------------------------
                if day <= mid:
                    consecutive += 1   # add to consecutive count

                    # If we collected k adjacent flowers,
                    # we can form one bouquet
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0   # reset for next bouquet

                else:
                    # --------------------------------------------------
                    # If flower has NOT bloomed yet (day > mid),
                    # we cannot use it.
                    # Also, adjacency breaks here.
                    # So reset consecutive count.
                    # --------------------------------------------------
                    consecutive = 0

            # --------------------------------------------------
            # 4️⃣ Adjust binary search
            # --------------------------------------------------

            if bouquets >= m:
                # We can make enough bouquets by day mid.
                # Try smaller day to minimize answer.
                right = mid
            else:
                # Not enough bouquets.
                # Need more days.
                left = mid + 1

        # When left == right, we found minimum day
        return left


# ------------------------------
# Example run (for local IDE)
# ------------------------------
if __name__ == "__main__":
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1

    sol = Solution()
    print("Minimum days needed:", sol.minDays(bloomDay, m, k))

# Time Complexity: O(n log D) , D = max(bloomDay)
# Space Complexity: O(1)
from typing import List
from collections import deque

class Solution:
    def firstNegative(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the first negative integer in every window of size k.
        If a window has no negative number, appends 0.
        """
        q = deque()  # stores indices of negative numbers in current window
        l, r = 0, 0  # left and right pointers of the sliding window
        output = []

        while r < len(nums):
            # 1️⃣ If current number is negative, store its index in deque
            # Example: nums = [12, -1, -7], r=1 -> nums[r] = -1, q = [1]
            if nums[r] < 0:
                q.append(r)

            # 2️⃣ Remove indices that are out of current window (left < l)
            # Example: window size k=3, l=1, q[0]=0 -> index 0 is out of window -> pop
            if q and q[0] < l:
                q.popleft()

            # 3️⃣ When window reaches size k, record result
            if r + 1 >= k:
                # a) If deque is not empty, front is first negative
                if q:
                    output.append(nums[q[0]])  # first negative in window
                # b) If deque is empty, no negatives -> append 0
                else:
                    output.append(0)

                # 4️⃣ Move left pointer for next window
                l += 1

            # 5️⃣ Expand window by moving right pointer
            r += 1

        return output


# Example
nums = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
sol = Solution()
print(sol.firstNegative(nums, k))
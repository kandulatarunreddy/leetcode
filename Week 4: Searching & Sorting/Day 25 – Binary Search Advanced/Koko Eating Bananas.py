import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
sol = Solution()
piles = [3,6,7,11]
h = 8
print(sol.minEatingSpeed(piles,h))
#Tc: O(n∗logm) sc:O(1), n is the length of the input array ,m is the maximum number of bananas in a pile
'''
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += (p + k - 1) // k   # avoid math.ceil give less TC

            if totalTime <= h:
                r = k-1
            else:
                l = k + 1

        return l
'''
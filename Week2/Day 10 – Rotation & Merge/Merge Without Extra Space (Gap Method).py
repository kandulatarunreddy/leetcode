import math

class Solution:
    def merge(self, arr1: list[int], arr2: list[int], m: int, n: int) -> None:
        gap = math.ceil((m + n) / 2)
        while gap > 0:
            i = 0
            j = gap
            while j < m + n:
                # i in arr1, j in arr1
                if i < m and j < m:
                    if arr1[i] > arr1[j]:
                        arr1[i], arr1[j] = arr1[j], arr1[i]
                # i in arr1, j in arr2
                elif i < m and j >= m:
                    if arr1[i] > arr2[j - m]: #i=3, j=4 so j-m =4-4=0
                        arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

                # i in arr2, j in arr2
                else:
                    if arr2[i - m] > arr2[j - m]:#i=4,j=5
                        arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

                i += 1
                j += 1

            if gap == 1:
                gap = 0
            else:
                gap = math.ceil(gap / 2)
a = [2, 4, 7, 10]
b = [2, 3]
Solution().merge(a, b, len(a), len(b))
print(a)  # [2, 2, 3, 4]
print(b)  # [7, 10]

#tc: O((m + n) log(m + n)) and sc:O(1)
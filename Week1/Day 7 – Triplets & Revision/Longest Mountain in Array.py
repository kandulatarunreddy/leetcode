from typing import List
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        i = 1

        while i < n - 1:
            # check if arr[i] is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l = i - 1
                r = i + 1
                # expand left
                while l > 0 and arr[l - 1] < arr[l]:
                    l -= 1
                # expand right
                while r < n - 1 and arr[r] > arr[r + 1]:
                    r += 1
                ans = max(ans, r - l + 1)
                i = r  # skip processed elements
            else:
                i += 1
        return ans

if __name__=="__main__":
    solution=Solution()
    arr = [2,1,4,7,3,2,5]
    print("Size of Mountain:",solution.longestMountain(arr))
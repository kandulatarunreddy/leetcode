from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        curmax,res=0,0
        while l<r:
            curmax=(r-l)*min(height[l],height[r])
            res=max(curmax,res)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res

if __name__ == "__main__":
    solution = Solution()

    height = [1,8,6,2,5,4,8,3,7]

    print("Input:", height)
    print("maxArea:", solution.maxArea(height))

#Tc: O(n) sc:O(1)



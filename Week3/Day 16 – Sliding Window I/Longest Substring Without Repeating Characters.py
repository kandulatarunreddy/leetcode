class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map=set()
        l=0
        r=0
        res=0
        while r<len(s):
            while s[r] in map:
                map.remove(s[l])
                l+=1
            map.add(s[r])
            res=max(res,r-l+1)
            r+=1
        return res

sol=Solution()
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))
#Tc:O(n) Sc:O(1)


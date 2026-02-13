from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        if len(p)>len(s):
            return res
        window,p_count=[0]*26,[0]*26

        for c in p:
            p_count[ord(c)-ord('a')]+=1

        l=0

        for r in range(len(s)):
            window[ord(s[r])-ord('a')]+=1
            if r-l+1>len(p):
                window[ord(s[l])-ord('a')]-=1
                l+=1
            if window==p_count:
                res.append(l)
        return res


sol=Solution()
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s,p))
#Tc:O(n) Sc:O(1)
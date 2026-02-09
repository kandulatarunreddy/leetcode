class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1,map2={},{}
        for i in range(len(s)):
            if (s[i] in map1 and map1[s[i]]!=t[i]) or(t[i] in map2 and map2[t[i]]!=s[i]) :
                return False
            map1[s[i]]=t[i]
            map2[t[i]]=s[i]
        return True

sol=Solution()
s = "f11"
t = "b23"
print(sol.isIsomorphic(s,t))
#Tc: O(n) Sc: O(n)
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
sol=Solution()
s = "sadbutsad"
t = "sad"
print(sol.strStr(s,t))
#Tc: O(n*m) Sc: O(m) Python slicing creates a new temporary string of size m each iteration.
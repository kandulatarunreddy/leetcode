class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # try deleting left OR right char
                return isPal(l+1, r) or isPal(l, r-1)
            l += 1
            r -= 1
        return True
sol=Solution()
s = "abca"
print(sol.validPalindrome(s))
#Tc:O(n) Sc:O(1)
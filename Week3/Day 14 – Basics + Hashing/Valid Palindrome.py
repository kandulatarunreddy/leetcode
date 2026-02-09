class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # skip non-alphanumeric left
            while l < r and not self.isAplhaNumeric(s[l]):
                l += 1
            # skip non-alphanumeric right
            while l < r and not self.isAplhaNumeric(s[r]):
                r -= 1
            # compare lowercase characters
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isAplhaNumeric(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

s = "A man, a plan, a canal: Panama"
sol=Solution()
print(sol.isPalindrome(s))
#Tc:O(n) Sc:O(1)

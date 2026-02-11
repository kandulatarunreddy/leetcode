class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ""

        for i in range(len(s)):
            p1 = expand_from_center(i, i)      # odd
            p2 = expand_from_center(i, i + 1)  # even
            longest = max(longest, p1, p2, key=len)

        return longest
sol=Solution()
s = "babad"
print(sol.longestPalindrome(s))
#Tc:O(n^2) Sc:O(1)

'''class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1            
            return s[left+1:right]

        longest = ""
        
        for i in range(len(s)):
            # 1) odd length palindrome (center at i)
            p1 = expand_from_center(i, i)
            # 2) even length palindrome (center between i and i+1)
            p2 = expand_from_center(i, i + 1)
            # choose the longer palindrome
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
        return longest'''
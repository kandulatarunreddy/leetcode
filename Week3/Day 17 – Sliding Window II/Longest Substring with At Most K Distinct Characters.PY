class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k == 0 or not s:
            return 0
        l = 0
        count = {}
        maxlen = 0

        for r in range(len(s)):
            # expand window
            count[s[r]] = 1+count.get(s[r], 0)

            # shrink window if > k distinct chars
            while len(count) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            # update answer
            maxlen = max(maxlen, r - l + 1)
        return maxlen
sol=Solution()
s = "eceba"
k=2
print(sol.lengthOfLongestSubstringKDistinct(s,k))
#Tc:O(n) Sc:O(k)
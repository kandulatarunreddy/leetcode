class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split words (ignores extra spaces)
        words = s.split()
        # Step 2: Reverse the list of words
        words.reverse()
        # Step 3: Join with a single space
        return ' '.join(words)

sol = Solution()
print(sol.reverseWords("the sky is blue"))
#Tc: O(n), Sc=O(n)
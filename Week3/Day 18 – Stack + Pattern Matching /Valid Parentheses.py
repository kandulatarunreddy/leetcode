class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in hashmap:  # If it's an opening bracket
                stack.append(char)
            else:  # It's a closing bracket
                if not stack or stack[-1] != hashmap[char]:
                    return False
                stack.pop()  # Remove the matched opening bracket

        return not stack  # True if stack is empty, False otherwise
sol=Solution()
s = "([])"
print(sol.isValid(s))
#TC:O(n), SC:O(n)
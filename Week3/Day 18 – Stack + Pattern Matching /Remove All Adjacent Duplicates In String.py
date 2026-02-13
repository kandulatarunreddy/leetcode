class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for c in s:
            if stack and stack[-1] ==c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
sol=Solution()
s = "abbaca"
result = sol.removeDuplicates(s)
print(result)  # Output: "ca"
#TC:O(n),SC:O(n)
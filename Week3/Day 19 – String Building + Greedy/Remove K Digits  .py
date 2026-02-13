class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)

        while stack and k:
            stack.pop()
            k -= 1

        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1

        res = stack[i:]
        return ''.join(res) if res else "0"
sol=Solution()
nums = "1432219"
k = 3
print(sol.removeKdigits(nums,k))
#Tc: O(n), sc:O(n)
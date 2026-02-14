class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        op='+'
        for i,c in enumerate(s):
            if c.isdigit():
                num=num*10+int(c)
            if c in '+-*/' or i==len(s)-1:
                if op=='+':
                    stack.append(num)
                elif op=='-':
                    stack.append(-num)
                elif op=='*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                op=c
                num=0
        return sum(stack)
sol=Solution()
s = "3+2*2"
print(sol.calculate(s))
#Tc: O(n) sc:O(n)



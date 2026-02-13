class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        cur_num = 0
        cur_str = ''
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)  # handle multi-digit numbers
            elif c == '[':
                num_stack.append(cur_num)
                str_stack.append(cur_str)
                cur_num = 0
                cur_str = ''
            elif c == ']':
                repeat = num_stack.pop()
                prev_str = str_stack.pop()
                cur_str = prev_str + cur_str * repeat
            else:
                cur_str += c
        return cur_str
sol=Solution()
s = "3[a]2[bc]"
result = sol.decodeString(s)
print(result)

#TC: O(m+n), SC:O(m+n)
#n = length of input string, m = length of decoded string(output)
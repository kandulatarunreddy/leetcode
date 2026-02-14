class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"                       # start sequence
        for _ in range(n-1):            # build next terms
            cur = []
            count = 1
            # compare current with previous
            for i in range(1, len(res)):
                if res[i] == res[i-1]:      # same digit
                    count += 1
                else:                       # digit changed
                    cur.append(str(count))
                    cur.append(res[i-1])
                    count = 1
                    # flush last group
            cur.append(str(count))
            cur.append(res[-1])
            res = "".join(cur)          # next term
        return res

sol=Solution()
n=4
print(sol.countAndSay(n))
#Time: O(n · m) Space: O(m) m is the length of the nth Count-and-Say string.
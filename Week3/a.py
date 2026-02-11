from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
strs.sort()
print(strs)

res = defaultdict(list)
count=[0,1,2,4]
s="eat"
res[tuple(count)].append(s)
print(res)

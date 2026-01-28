def longestSubarray(arr, k):
    prefixsum=0
    map={}
    res=0
    for i,n in enumerate(arr):
        prefixsum+=n
        if prefixsum==k:
            res=i+1
        elif (prefixsum-k) in map:
            res=max(res,i-map[prefixsum-k])

        if prefixsum not in map:
            map[prefixsum]=i
    return res

if __name__ == "__main__":
    arr = [10, 5, 2, 7, 1, -10]
    k = 15
    print(longestSubarray(arr, k))

#O(n) Time and O(n) Space
def longestSubarrayEqual01(arr):
    prefixsum = 0
    mp = {}
    res = 0

    for i, n in enumerate(arr):
        # convert 0 to -1, 1 stays +1
        prefixsum += -1 if n == 0 else 1

        # sum == 0 means equal 0s and 1s from start
        if prefixsum == 0:
            res = i + 1
        elif prefixsum in mp:
            res = max(res, i - mp[prefixsum])

        # store first occurrence
        if prefixsum not in mp:
            mp[prefixsum] = i

    return res

if __name__ == "__main__":
    arr = [0, 1, 0, 1, 1, 0, 0]
    print(longestSubarrayEqual01(arr))

#O(n) Time and O(n) Space
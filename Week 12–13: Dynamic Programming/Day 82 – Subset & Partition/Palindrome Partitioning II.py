def minCut(s):
    n = len(s)

    # ----------------------------------------
    # Step 1: Precompute palindrome table
    # isPal[i][j] = True if substring s[i:j] is palindrome
    #
    # Example: s = "aab"
    # isPal[0][0] = True  -> "a"
    # isPal[0][1] = True  -> "aa"
    # isPal[1][2] = False -> "ab"
    # isPal[2][2] = True  -> "b"
    # ----------------------------------------
    isPal = [[False] * n for _ in range(n)]

    for end in range(n):
        for start in range(end + 1):
            # Condition:
            # 1. Characters match
            # 2. Inner substring is palindrome OR length <= 2
            #
            # Examples:
            # "a" → start == end → palindrome
            # "aa" → length 2 → palindrome if chars equal
            # "aba" → check middle part
            if s[start] == s[end] and (end - start <= 2 or isPal[start + 1][end - 1]):
                isPal[start][end] = True

    # ----------------------------------------
    # Step 2: DP array
    # dp[i] = minimum cuts needed for substring s[0:i]
    #
    # Example: s = "aab"
    # dp[0] = 0 ("a")
    # dp[1] = 0 ("aa")
    # dp[2] = 1 ("aa | b")
    # ----------------------------------------
    dp = [0] * n

    for i in range(n):
        # Worst case: cut before every character
        # Example: "abc" → a|b|c → 2 cuts
        dp[i] = i

        for j in range(i + 1):
            # If substring s[j:i] is palindrome
            if isPal[j][i]:

                if j == 0:
                    # Whole substring is palindrome
                    # Example: "aa"
                    dp[i] = 0
                else:
                    # Cut before j
                    # Example: "aa|b"
                    # dp[i] = dp[j-1] + 1
                    dp[i] = min(dp[i], dp[j - 1] + 1)

    return dp[n - 1]


# ----------------------------------------
# Driver Code
# ----------------------------------------
if __name__ == "__main__":

    # Example 1
    s1 = "aab"
    # Best partition: "aa | b"
    # Cuts = 1
    print("Input:", s1)
    print("Minimum cuts:", minCut(s1))
    print()

    # Example 2
    s2 = "abc"
    # Only single letters are palindromes
    # Partition: a | b | c
    # Cuts = 2
    print("Input:", s2)
    print("Minimum cuts:", minCut(s2))
    print()

    # Example 3
    s3 = "aabaa"
    # Whole string is palindrome
    # Cuts = 0
    print("Input:", s3)
    print("Minimum cuts:", minCut(s3))


# ----------------------------------------
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# ----------------------------------------
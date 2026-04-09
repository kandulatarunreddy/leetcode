def wordBreak(s: str, wordDict: list[str]) -> bool:
    """
    Time Complexity:
        Outer loop  -> O(n)
        Inner loop  -> O(n)
        Substring   -> O(n)
        Total       -> O(n^3) in Python

    Space Complexity:
        dp array -> O(n)
        word set -> O(m)  (m = total dictionary size)
        Total    -> O(n + m) ≈ O(n)
    """

    word_set = set(wordDict)   # O(1) lookup
    n = len(s)

    # dp[i] means s[0:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):        # O(n)
        for j in range(i):            # O(n)
            if dp[j] and s[j:i] in word_set:   # slicing O(n)
                dp[i] = True
                break

    return dp[n]


# -------- main method (IDE runnable) --------
if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]

    print("Input string :", s)
    print("Dictionary   :", wordDict)

    result = wordBreak(s, wordDict)

    print("Word Break possible:", result)
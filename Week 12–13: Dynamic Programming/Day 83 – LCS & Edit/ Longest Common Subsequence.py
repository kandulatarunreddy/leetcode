def lcs_length(s1: str, s2: str) -> int:
    """
    Compute the length of the Longest Common Subsequence (LCS)
    between two strings using Dynamic Programming (space optimized).
    """

    # Step 1: Ensure s2 is the smaller string
    # This helps reduce space usage (we only store DP for s2)
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    # Step 2: Initialize previous row of DP table
    # prev[j] represents LCS length for:
    # s1[0...i-2] and s2[0...j-1]
    prev = [0] * (len(s2) + 1)

    # Step 3: Iterate through each character of s1
    for i in range(1, len(s1) + 1):

        # Current row for DP
        curr = [0] * (len(s2) + 1)

        # Step 4: Iterate through each character of s2
        for j in range(1, len(s2) + 1):

            # Case 1: Characters match
            # If s1[i-1] == s2[j-1], we extend the LCS found so far
            # by adding this matching character
            # Example:
            # s1[i-1] = 'a', s2[j-1] = 'a'
            if s1[i - 1] == s2[j - 1]:
                # Take diagonal value + 1
                # Example:
                # prev[j-1] = 0 → curr[j] = 1
                curr[j] = prev[j - 1] + 1

            # Case 2: Characters do not match
            # We take the maximum of:
            # 1. Ignoring current char of s1 → prev[j]
            # 2. Ignoring current char of s2 → curr[j-1]
            else:
                # If not match, take max of:
                # - top (prev[j])
                # - left (curr[j-1])
                # Example:
                # prev[j] = 1, curr[j-1] = 1 → curr[j] = 1
                curr[j] = max(prev[j], curr[j - 1])

        # Step 5: Update previous row for next iteration
        print("CUR:",curr)
        prev = curr

    # Step 6: The last value contains the final LCS length
    return prev[-1]


# =========================
# 🚀 DRIVER CODE
# =========================
if __name__ == "__main__":

    # Example inputs
    s1 = "abcde"
    s2 = "ace"

    # Function call
    result = lcs_length(s1, s2)

    # Output result
    print("String 1:", s1)
    print("String 2:", s2)
    print("LCS Length:", result)


"""
=========================
Time & Space Complexity
=========================

Time Complexity (TC):
O(m × n)
Where m = length of s1, n = length of s2
We iterate through both strings using nested loops.

Space Complexity (SC):
O(min(m, n))
We only store two rows (prev and curr) of size equal to the smaller string.
"""
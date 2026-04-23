def longest_palindrome(s):
    """
    Returns the longest palindromic substring in s.
    """

    n = len(s)
    start = 0
    max_len = 0

    # Helper function to expand around center
    def expand(left, right):
        nonlocal start, max_len

        # Expand while valid palindrome
        while left >= 0 and right < n and s[left] == s[right]:
            current_len = right - left + 1

            # Update longest palindrome found
            if current_len > max_len:
                start = left
                max_len = current_len

            left -= 1
            right += 1

    for i in range(n):
        # Odd-length palindrome
        expand(i, i)

        # Even-length palindrome
        expand(i, i + 1)

    return s[start:start + max_len]


# Example usage
if __name__ == "__main__":
    s = "babad"
    print(longest_palindrome(s))  # Output: "bab" or "aba"


# Time Complexity: O(n^2)
# Space Complexity: O(1)
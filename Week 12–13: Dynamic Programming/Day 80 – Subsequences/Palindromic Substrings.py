def count_substrings(s):
    """
    Returns the number of palindromic substrings in string s.
    """

    n = len(s)
    count = 0

    # Helper function to expand around center
    def expand(left, right):
        nonlocal count  # allows modifying outer 'count'

        # Expand while substring is a palindrome
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(n):
        # Odd-length palindromes (center at i)
        expand(i, i)

        # Even-length palindromes (center between i and i+1)
        expand(i, i + 1)

    return count


# Example usage
if __name__ == "__main__":
    s = "aaa"
    print(count_substrings(s))  # Output: 6


# Time Complexity: O(n^2)
# Space Complexity: O(1)
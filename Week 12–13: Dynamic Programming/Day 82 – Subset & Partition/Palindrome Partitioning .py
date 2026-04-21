def partition(s):
    result = []
    path = []

    # Helper function to check palindrome
    def isPalindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    # Backtracking function
    def backtrack(start):
        # If we reach end → valid partition
        if start == len(s):
            result.append(path[:])
            return

        # Try all possible cuts
        for end in range(start, len(s)):
            # If substring is palindrome
            if isPalindrome(start, end):
                # Choose
                path.append(s[start:end+1])

                # Explore
                print("backtrack:",end+1)
                backtrack(end + 1)
                print("Path:",path)
                # Backtrack
                path.pop()

    backtrack(0)
    return result


# -------------------------
# Driver code
# -------------------------
if __name__ == "__main__":
    s = "aab"
    ans = partition(s)

    print("All palindrome partitions:")
    for p in ans:
        print(p)


# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)
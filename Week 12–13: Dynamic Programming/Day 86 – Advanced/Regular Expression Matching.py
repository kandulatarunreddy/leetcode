class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # cache[(i, j)] will store whether s[i:] matches p[j:]
        # This avoids recomputing same states (memoization)
        cache = {}

        def dfs(i, j):
            # If we already computed this state, return stored result
            if (i, j) in cache:
                return cache[(i, j)]

            # If both string and pattern are fully matched
            if i >= len(s) and j >= len(p):
                return True

            # If pattern finished but string still remains → not match
            if j >= len(p):
                return False

            # Check if current characters match
            # Conditions:
            # 1. string index still valid
            # 2. characters equal OR pattern has '.'
            match = (
                    i < len(s) and
                    (s[i] == p[j] or p[j] == ".")
            )

            # Handle "*" wildcard
            # Example: "a*" or ".*"
            # '*' means zero or more of previous char
            if (j + 1) < len(p) and p[j + 1] == "*":

                # Two choices:
                # 1. Skip this "char*" completely  -> dfs(i, j+2)
                # 2. If characters match, use one char from string -> dfs(i+1, j)
                cache[(i, j)] = (
                        dfs(i, j + 2) or
                        (match and dfs(i + 1, j))
                )
                return cache[(i, j)]

            # If no '*' and characters match,
            # move both pointers forward
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # Otherwise characters don't match
            cache[(i, j)] = False
            return False

        # Start matching from beginning of both string and pattern
        return dfs(0, 0)

if __name__ == "__main__":
    sol = Solution()
    s = "ab"
    p = ".*"
    print(sol.isMatch(s,p))

#Time: O(m × n) , Space: O(m × n)
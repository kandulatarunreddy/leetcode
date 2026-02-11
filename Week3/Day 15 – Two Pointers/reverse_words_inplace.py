def reverse_words_inplace(s: list[str]) -> None:
    n = len(s)
    # Step 1: Reverse the whole string
    reverse_range(0, n - 1)

    # Step 2: Reverse each word
    start = 0
    for end in range(n + 1):
        if end == n or s[end] == ' ':
            reverse_range(start, end - 1)
            start = end + 1

def reverse_range(left: int, right: int) -> None:
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Example usage
s = list(" the sky is blue ")
reverse_words_inplace(s)
print("".join(s))  # Output: "blue is sky the"

#Tc: O(n) Sc:O(1)
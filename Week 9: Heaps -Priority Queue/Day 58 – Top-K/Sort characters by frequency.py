from collections import Counter


def frequencySort(s: str) -> str:
    """
    Sort characters in descending order of frequency.

    Example:
    Input:  "tree"
    Output: "eert" or "eetr"
    """

    # ---------------------------------------------------
    # Step 1:
    # Count frequency of each character
    #
    # Example:
    # s = "tree"
    #
    # freq = {
    #   't': 1,
    #   'r': 1,
    #   'e': 2
    # }
    # ---------------------------------------------------
    freq = Counter(s)

    # ---------------------------------------------------
    # Step 2:
    # Create buckets where index = frequency
    #
    # Since max frequency can be len(s),
    # create len(s) + 1 buckets
    #
    # Example:
    # buckets[2] = ['e']
    # buckets[1] = ['t', 'r']
    # ---------------------------------------------------
    buckets = [[] for _ in range(len(s) + 1)]

    # ---------------------------------------------------
    # Step 3:
    # Place each character into its frequency bucket
    # ---------------------------------------------------
    for char, count in freq.items():
        buckets[count].append(char)

    # ---------------------------------------------------
    # Step 4:
    # Traverse buckets from high frequency to low
    # ---------------------------------------------------
    result = []

    for count in range(len(s), 0, -1):

        # Multiple chars may have same frequency
        for char in buckets[count]:

            # Repeat character "count" times
            #
            # Example:
            # 'e' * 2 = "ee"
            result.append(char * count)

    # Join all parts into final string
    return ''.join(result)


# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------

s = "tree"

print(frequencySort(s))

# Time Complexity: O(n)
# Space Complexity: O(n)
def edit_distance(s1: str, s2: str) -> int:
    """
    Compute the minimum number of operations required to convert
    string s1 into string s2.
    Allowed operations: insert, delete, replace
    """

    # Step 1: Initialize previous row
    # prev[j] = edit distance between "" and s2[0...j-1]
    # Example: "" → "abc" needs 0,1,2,3 insertions
    prev = list(range(len(s2) + 1))

    # Step 2: Iterate through s1
    for i in range(1, len(s1) + 1):

        # First column: converting s1[0...i-1] → ""
        # requires i deletions
        curr = [i] + [0] * len(s2)

        # Step 3: Iterate through s2
        for j in range(1, len(s2) + 1):

            # Case 1: Characters match → no operation needed
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]

            else:
                # Case 2: Characters do not match
                # We take minimum of 3 operations:

                insert_op = curr[j - 1]   # Insert into s1
                delete_op = prev[j]       # Delete from s1
                replace_op = prev[j - 1]  # Replace character

                curr[j] = 1 + min(insert_op, delete_op, replace_op)

        # Move current row to previous
        prev = curr

    # Final answer
    return prev[len(s2)]


# =========================
# 🚀 DRIVER CODE
# =========================
if __name__ == "__main__":

    s1 = "horse"
    s2 = "ros"

    result = edit_distance(s1, s2)

    print("String 1:", s1)
    print("String 2:", s2)
    print("Edit Distance:", result)


"""
=========================
Example Explanation
=========================

s1 = "horse"
s2 = "ros"

Operations:
horse → rorse  (replace 'h' → 'r')
rorse → rose   (delete 'r')
rose → ros     (delete 'e')

Total = 3 operations

=========================
Time Complexity (TC):
O(len(s1) × len(s2))

Space Complexity (SC):
O(len(s2))
"""
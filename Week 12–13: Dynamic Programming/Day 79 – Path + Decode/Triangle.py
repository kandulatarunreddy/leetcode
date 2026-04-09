# Start from the second last row and move upward.
# For each element, add the minimum of the two adjacent numbers from the row below.

def minimumTotal(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(
                triangle[i+1][j],
                triangle[i+1][j+1]
            )
    return triangle[0][0]


if __name__ == "__main__":
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    result = minimumTotal(triangle)
    print("Minimum Path Sum:", result)

# Time Complexity: O(n^2)
# Space Complexity: O(1)  (in-place modification)
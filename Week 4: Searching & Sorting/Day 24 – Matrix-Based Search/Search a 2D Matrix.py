from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # number of rows and columns
        rows, cols = len(matrix), len(matrix[0])

        # binary search boundaries: flatten the matrix indices from 0 to rows*cols-1
        l, r = 0, rows * cols - 1

        # standard binary search
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // cols  # compute row index
            col = mid % cols   # compute column index
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]

    print(sol.searchMatrix(matrix, 3))    # True
    print(sol.searchMatrix(matrix, 13))   # False
    print(sol.searchMatrix(matrix, 60))   # True
    print(sol.searchMatrix(matrix, 0))    # False

# Time Complexity: O(log(m * n)) where m = rows, n = cols
# Space Complexity: O(1)
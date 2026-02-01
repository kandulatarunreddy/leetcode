from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Get matrix dimensions
        ROWS, COLS = len(matrix), len(matrix[0])

        # Flag to track whether the first row needs to be zeroed
        rowZero = False

        # First pass: use first row and first column as markers
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # Mark the column to be zeroed
                    matrix[0][c] = 0

                    if r > 0:
                        # Mark the row to be zeroed (if not first row)
                        matrix[r][0] = 0
                    else:
                        # If zero is in the first row, remember it separately
                        rowZero = True

        # Second pass: zero out cells based on markers
        # Skip first row and first column for now
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # If matrix[0][0] is zero, zero out the entire first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # If the first row originally had a zero, zero it out
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

matrix = [[0, 1]]

sol = Solution()
sol.setZeroes(matrix)
print(matrix)



from typing import List
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse rows manually
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
sol.rotate(matrix)
print(matrix)
#Time Complexity: O(n²) Space Complexity: O(1)
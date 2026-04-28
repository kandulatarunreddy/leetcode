class Solution:
    def pacificAtlantic(self, heights):
        # If grid is empty, no result
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        # These sets store cells reachable from each ocean
        pacific = set()
        atlantic = set()

        # DFS function to explore reachable cells
        def dfs(r, c, visited, prev_height):
            # Stop if:
            # - Out of bounds
            # - Already visited
            # - Water cannot flow uphill (current height < previous height)
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                    (r, c) in visited or
                    heights[r][c] < prev_height):
                return

            # Mark current cell as reachable from this ocean
            visited.add((r, c))

            # Explore all 4 directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # -------------------------------
        # Step 1: Run DFS from Pacific borders
        # Pacific touches top row and left column
        # -------------------------------

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])        # left column

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])        # top row

        # -------------------------------
        # Step 2: Run DFS from Atlantic borders
        # Atlantic touches bottom row and right column
        # -------------------------------

        for r in range(rows):
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # right column

        for c in range(cols):
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # bottom row

        # -------------------------------
        # Step 3: Intersection
        # Cells reachable from BOTH oceans
        # -------------------------------

        return [list(cell) for cell in(pacific & atlantic)]
if __name__ == "__main__":
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]

    result = Solution().pacificAtlantic(heights)

    print("Cells that can flow to both oceans:",result)


# Time Complexity: O(m * n)
# Space Complexity: O(m * n) (visited sets + recursion stack)
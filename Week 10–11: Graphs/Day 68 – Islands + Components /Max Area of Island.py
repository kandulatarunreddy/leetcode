def max_area_of_island(grid):
    """
    Return the maximum area of an island

    Time Complexity: O(m * n)
        - Each cell is visited once

    Space Complexity: O(m * n) worst case (recursion stack)
    """

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs(r, c):
        # Base case: out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0

        # Mark as visited
        grid[r][c] = 0

        # Current cell contributes 1 + neighbors
        area = 1

        # Explore all 4 directions
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)

        return area

    # Traverse grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))

    return max_area
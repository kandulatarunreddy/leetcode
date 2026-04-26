def num_islands_dfs(grid):
    """
    Count number of islands using DFS

    Time Complexity: O(m * n)
        - Each cell is visited at most once

    Space Complexity: O(m * n) (worst case recursion stack)
        - In worst case (all land), recursion depth can go up to m*n
    """

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def dfs(r, c):
        # Base case: out of bounds OR water cell
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        # Mark current cell as visited by sinking the land
        grid[r][c] = '0'

        # Visit all 4 adjacent directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    # Traverse the grid
    for r in range(rows):
        for c in range(cols):
            # If land is found, it's a new island
            if grid[r][c] == '1':
                island_count += 1
                dfs(r, c)  # explore entire island

    return island_count

from collections import deque

def num_islands_bfs(grid):
    """
    Count number of islands using BFS (queue)

    Time Complexity: O(m * n)
        - Each cell is processed once

    Space Complexity: O(min(m, n)) to O(m * n)
        - Queue can grow up to size of island in worst case
    """

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))

        # Mark starting cell as visited
        grid[r][c] = '0'

        while queue:
            row, col = queue.popleft()

            # Check all 4 directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc

                # If within bounds and it's land
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'  # mark visited

    # Traverse grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                island_count += 1
                bfs(r, c)

    return island_count

if __name__ == "__main__":
    grid1 = [
        ['1', '1', '0', '0'],
        ['1', '0', '0', '1'],
        ['0', '0', '1', '1'],
        ['0', '0', '0', '0']
    ]

    # Important: make a copy because grid gets modified
    import copy

    print("DFS Output:", num_islands_dfs(copy.deepcopy(grid1)))
    print("BFS Output:", num_islands_bfs(copy.deepcopy(grid1)))
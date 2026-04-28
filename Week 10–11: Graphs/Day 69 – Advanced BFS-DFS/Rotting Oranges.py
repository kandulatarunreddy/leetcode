from collections import deque

class Solution:
    def orangesRotting(self, grid):
        # If grid is empty, return -1
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Find all initial rotten oranges and count fresh ones
        # We do multi-source BFS, so all rotten oranges start in queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))  # rotten orange source
                elif grid[r][c] == 1:
                    fresh += 1           # count fresh oranges

        # Directions for moving up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        minutes = 0

        # Step 2: BFS traversal (level by level = each minute)
        while queue and fresh > 0:
            # Process all oranges in current minute
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # Try infecting all 4 adjacent cells
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # If neighbor is a fresh orange, rot it
                    if (0 <= nr < rows and 0 <= nc < cols and
                            grid[nr][nc] == 1):

                        grid[nr][nc] = 2      # mark as rotten
                        queue.append((nr, nc)) # add to BFS queue(add newly rotten orange)
                        fresh -= 1            # one less fresh orange

            # After processing one level, increment time
            minutes += 1

        # If fresh oranges still remain, it's impossible
        return minutes if fresh == 0 else -1

# ---------------- RUN CODE ----------------
if __name__ == "__main__":
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]

    result = Solution().orangesRotting(grid)
    print("Minutes to rot all oranges:", result)


# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
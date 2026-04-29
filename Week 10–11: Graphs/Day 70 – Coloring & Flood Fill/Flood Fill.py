from collections import deque

def flood_fill(image, sr, sc, new_color):
    """
    Perform flood fill on a 2D image starting from (sr, sc).

    :param image: List[List[int]] -> 2D grid of colors
    :param sr: int -> starting row
    :param sc: int -> starting column
    :param new_color: int -> color to fill with
    :return: Modified image after flood fill
    """

    # Get dimensions of the grid
    rows, cols = len(image), len(image[0])

    # Store the original color at the starting cell
    start_color = image[sr][sc]

    # Edge case:
    # If the starting color is already the new color,
    # no need to process (prevents infinite loop)
    if start_color == new_color:
        return image

    # Initialize queue for BFS and add starting cell
    queue = deque()
    queue.append((sr, sc))

    # Change the starting cell color to new_color
    # This also acts as marking it as "visited"
    image[sr][sc] = new_color

    # Directions for 4-connected neighbors (down, up, right, left)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # BFS traversal
    while queue:
        # Pop the front cell from queue
        r, c = queue.popleft()

        # Explore all 4 neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check:
            # 1. Within grid bounds
            # 2. Same as original color (so it should be filled)
            if 0 <= nr < rows and 0 <= nc < cols:
                if image[nr][nc] == start_color:
                    # Fill the neighbor with new color
                    image[nr][nc] = new_color

                    # Add neighbor to queue for further exploration
                    queue.append((nr, nc))

    # Return the updated image
    return image


# --------- Example Run ---------
if __name__ == "__main__":
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    sr, sc = 1, 1
    new_color = 2

    result = flood_fill(image, sr, sc, new_color)

    print("Filled Image:")
    for row in result:
        print(row)

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
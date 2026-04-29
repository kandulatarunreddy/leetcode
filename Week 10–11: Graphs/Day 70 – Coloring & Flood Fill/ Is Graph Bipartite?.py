from collections import deque

def is_bipartite(graph):
    """
    Check if a graph is bipartite using BFS.

    :param graph: List[List[int]] -> adjacency list
                   graph[i] contains neighbors of node i
    :return: True if bipartite, else False
    """

    n = len(graph)

    # रंग array: -1 = not colored, 0 and 1 are the two colors
    color = [-1] * n

    # Loop through all nodes (important for disconnected graph)
    for start in range(n):

        # If node is already colored, skip
        if color[start] != -1:
            continue

        # Start BFS from this node
        queue = deque([start])

        # Assign first color (0)
        color[start] = 0

        while queue:
            node = queue.popleft()

            # Traverse all neighbors
            for neighbor in graph[node]:

                # If neighbor is not colored
                if color[neighbor] == -1:
                    # Assign opposite color
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)

                # If neighbor has same color → conflict
                elif color[neighbor] == color[node]:
                    return False

    # If no conflicts found
    return True


# --------- Example Run ---------
if __name__ == "__main__":
    graph = [
        [1, 3],  # node 0
        [0, 2],  # node 1
        [1, 3],  # node 2
        [0, 2]   # node 3
    ]

    print("Is Bipartite:", is_bipartite(graph))

# Time Complexity: O(V + E)
# Space Complexity: O(V)
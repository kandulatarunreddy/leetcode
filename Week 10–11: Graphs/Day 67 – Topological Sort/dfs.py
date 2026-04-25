def topo_sort_dfs(graph):
    """
    Topological Sort using DFS (stack method)
    """

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

        # Add to stack after visiting all neighbors (postorder)
        stack.append(node)

    # Handle disconnected graph
    for node in graph:
        if node not in visited:
            dfs(node)

    # Reverse stack to get correct order
    return stack[::-1]


# ---------------- Example Graph ----------------
if __name__ == "__main__":
    graph = {
        5: [2, 0],
        4: [0, 1],
        2: [3],
        3: [1],
        1: [],
        0: []
    }
    print("Topological Sort (DFS):", topo_sort_dfs(graph))


# Time Complexity: O(V + E)
# Space Complexity: O(V)
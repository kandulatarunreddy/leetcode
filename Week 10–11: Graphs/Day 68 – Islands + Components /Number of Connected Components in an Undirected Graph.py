def count_components(n, edges):
    """
    Count connected components in an undirected graph

    Time Complexity: O(V + E)
        - Each node and edge is visited once

    Space Complexity: O(V + E)
        - adjacency list + visited set + recursion stack
    """

    # Build adjacency list
    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        # Mark node as visited
        visited.add(node)

        # Visit all neighbors
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)

    components = 0

    # Try starting DFS from every node
    for i in range(n):
        if i not in visited:
            components += 1   # new component found
            dfs(i)

    return components
if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]

    result = count_components(n, edges)
    print("Number of Connected Components:", result)


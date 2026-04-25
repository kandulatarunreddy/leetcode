from collections import deque

def topo_sort_kahn(graph):
    """
    Topological Sort using Kahn's Algorithm (BFS)

    graph: adjacency list (dict)
    """

    # Step 1: Compute in-degree of each node
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Step 2: Add nodes with in-degree 0 to queue
    queue = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    topo_order = []

    # Step 3: Process queue
    while queue:
        node = queue.popleft()
        topo_order.append(node)

        # reduce in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

            # if in-degree becomes 0, add to queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check for cycle
    if len(topo_order) != len(graph):
        return "Cycle detected, topological sort not possible"

    return topo_order


# ----------- Example -----------
graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}

print("Topological Order:", topo_sort_kahn(graph))
#Time Complexity: O(V + E)
#Space Complexity: O(V)
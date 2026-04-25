def has_cycle_directed(graph):
    """
    Detect cycle in a directed graph using DFS + recursion stack.

    graph: adjacency list (dictionary)
    """

    visited = set()     # nodes that are fully processed
    rec_stack = set()   # nodes currently in DFS path (active recursion stack)

    def dfs(node):

        # 1. Mark node as visited and add to current recursion path
        visited.add(node)
        rec_stack.add(node)

        # 2. Explore all outgoing edges
        for neighbor in graph[node]:

            # CASE 1: If neighbor is not visited → go deeper
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

            # CASE 2: If neighbor is in current recursion path → cycle found
            elif neighbor in rec_stack:
                return True

        # 3. Backtracking step → remove node from current path
        rec_stack.remove(node)

        return False

    # 4. Handle disconnected graph (multiple components)
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


# ------------------ EXAMPLE 1 (CYCLE EXISTS) ------------------
graph1 = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]   # cycle: 1 → 2 → 3 → 1
}

print("Graph1 has cycle:", has_cycle_directed(graph1))


# ------------------ EXAMPLE 2 (NO CYCLE) ------------------
graph2 = {
    0: [1],
    1: [2],
    2: [3],
    3: []   # no cycle
}

print("Graph2 has cycle:", has_cycle_directed(graph2))


# Time Complexity: O(V + E)  # each node and edge is visited once
# Space Complexity: O(V)     # visited set + recursion stack
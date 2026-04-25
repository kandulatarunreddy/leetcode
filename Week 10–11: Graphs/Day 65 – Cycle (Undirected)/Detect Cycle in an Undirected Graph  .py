def has_cycle_undirected(graph):
    """
    Detect cycle in an undirected graph using DFS
    graph: adjacency list (dictionary)
    """

    visited = set()  # stores all visited nodes

    def dfs(node, parent):
        """
        node   → current node being visited
        parent → node from which we came (to avoid false cycle detection)
        """

        visited.add(node)  # mark current node as visited

        # explore all adjacent nodes
        for neighbor in graph[node]:

            # CASE 1: If neighbor is not visited, go deeper
            if neighbor not in visited:
                # if deeper call finds cycle, propagate True upward
                if dfs(neighbor, node):
                    return True

            # CASE 2: neighbor already visited AND not parent → cycle found
            elif neighbor != parent:
                return True

        # no cycle found from this node
        return False

    # handle disconnected graph (multiple components)
    for node in graph:
        if node not in visited:
            if dfs(node, -1):  # -1 means no parent for starting node
                return True

    return False


# Example usage
if __name__ == "__main__":
    graph = {
        0: [1],
        1: [0, 2, 3],
        2: [1, 3],
        3: [1, 2]
    }

    print(has_cycle_undirected(graph))
#Time Complexity: O(V + E)  # each node and edge is visited once
#Space Complexity: O(V)     # visited set + recursion stack
def dfs_recursive(graph, node, visited=None):
    """
    Recursive DFS

    TC: O(V + E)
    SC: O(V)  (visited + recursion stack)
    """
    if visited is None:
        visited = set()

    # base case
    if node in visited:
        return

    # mark visited
    visited.add(node)
    print(node, end=" ")

    # explore neighbors
    for neighbor in graph[node]:
        dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    """
    Iterative DFS using stack

    TC: O(V + E)
    SC: O(V)
    """
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            # reverse to maintain same order as recursion
            stack.extend(reversed(graph[node]))

def dfs_disconnected(graph):
    """
    Handles graphs with multiple components

    TC: O(V + E)
    SC: O(V)
    """
    visited = set()

    for node in graph:
        if node not in visited:
            print(f"\nComponent starting at {node}:")

            stack = [node]

            while stack:
                curr = stack.pop()

                if curr not in visited:
                    visited.add(curr)
                    print(curr, end=" ")

                    stack.extend(reversed(graph[curr]))


def dfs_path(graph, start, target):
    """
    Find ONE path from start → target

    TC: O(V + E)
    SC: O(V)
    """
    path = []
    visited = set()

    def dfs(node):
        if node in visited:
            return False

        visited.add(node)
        path.append(node)

        if node == target:
            return True

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        # backtrack
        path.pop()
        return False

    dfs(start)
    return path

def has_cycle_undirected(graph):
    """
    Detect cycle in undirected graph

    TC: O(V + E)
    SC: O(V)
    """
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True

    return False

def has_cycle_directed(graph):
    """
    Detect cycle in directed graph

    TC: O(V + E)
    SC: O(V)
    """
    visited = set()
    recursion_stack = set()

    def dfs(node):
        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

if __name__ == "__main__":

    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [],
        4: [5],   # disconnected component
        5: []
    }

    print("Recursive DFS:")
    dfs_recursive(graph, 0)

    print("\n\nIterative DFS:")
    dfs_iterative(graph, 0)

    print("\n\nDisconnected Graph DFS:")
    dfs_disconnected(graph)

    print("\n\nPath from 0 to 3:")
    print(dfs_path(graph, 0, 3))

    print("\nCycle (Undirected check):")
    print(has_cycle_undirected(graph))

    print("\nCycle (Directed check):")
    print(has_cycle_directed(graph))
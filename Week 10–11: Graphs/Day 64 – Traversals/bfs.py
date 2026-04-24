"""
BREADTH-FIRST SEARCH (BFS)

- Traverses level by level (neighbors first)
- Uses a QUEUE (FIFO)

Key Idea:
Visit all neighbors before going deeper

Time Complexity:
- O(V + E)

Space Complexity:
- O(V)

Where BFS is used:
- Shortest path (unweighted graph)
- Level order traversal
- Finding minimum steps
"""
from collections import deque

def bfs(graph, start):
    """
    Basic BFS traversal

    TC: O(V + E)
    SC: O(V)
    """
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()  # FIFO
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

from collections import deque

def bfs_disconnected(graph):
    """
    BFS for graphs with multiple components

    TC: O(V + E)
    SC: O(V)
    """
    visited = set()

    for start in graph:
        if start not in visited:
            print(f"\nComponent starting at {start}:")

            queue = deque([start])
            visited.add(start)

            while queue:
                node = queue.popleft()
                print(node, end=" ")

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
from collections import deque

def bfs_shortest_path(graph, start, target):
    """
    Finds shortest path in unweighted graph

    TC: O(V + E)
    SC: O(V)
    """
    queue = deque([start])
    visited = set([start])
    parent = {start: None}  # to reconstruct path

    while queue:
        node = queue.popleft()

        if node == target:
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    # reconstruct path
    path = []
    curr = target

    while curr is not None:
        path.append(curr)
        curr = parent.get(curr)

    path.reverse()
    return path

from collections import deque

def bfs_levels(graph, start):
    """
    BFS level-wise traversal

    TC: O(V + E)
    SC: O(V)
    """
    visited = set([start])
    queue = deque([start])

    level = 0

    while queue:
        size = len(queue)
        print(f"\nLevel {level}:", end=" ")

        for _ in range(size):
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        level += 1
if __name__ == "__main__":

    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [],
        4: [5],   # disconnected
        5: []
    }

    print("Basic BFS:")
    bfs(graph, 0)

    print("\n\nDisconnected BFS:")
    bfs_disconnected(graph)

    print("\n\nShortest path 0 → 3:")
    print(bfs_shortest_path(graph, 0, 3))

    print("\n\nLevel Order BFS:")
    bfs_levels(graph, 0)
from collections import deque


# Definition for a Node
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def cloneGraph(node):
    """
    Clone an undirected graph using BFS
    """

    # -----------------------------
    # Step 1: Edge case
    # -----------------------------
    if not node:
        return None

    # -----------------------------
    # Step 2: HashMap to store cloned nodes
    # Key: original node
    # Value: cloned node
    # -----------------------------
    clones = {}

    # -----------------------------
    # Step 3: Initialize BFS
    # -----------------------------
    queue = deque([node])

    # Create clone of starting node
    clones[node] = Node(node.val)

    # -----------------------------
    # Step 4: BFS traversal
    # -----------------------------
    while queue:
        curr = queue.popleft()

        # Traverse all neighbors of current node
        for nei in curr.neighbors:

            # If neighbor is not cloned yet
            if nei not in clones:
                # Create clone of neighbor
                clones[nei] = Node(nei.val)

                # Add neighbor to queue for BFS
                queue.append(nei)

            # Add the cloned neighbor to current cloned node
            clones[curr].neighbors.append(clones[nei])

    # -----------------------------
    # Step 5: Return cloned graph
    # -----------------------------
    return clones[node]


# -----------------------------
# Helper function to print graph (BFS)
# -----------------------------
def print_graph(node):
    visited = set()
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        if curr in visited:
            continue

        visited.add(curr)

        print(f"Node {curr.val} -> {[n.val for n in curr.neighbors]}")

        for nei in curr.neighbors:
            if nei not in visited:
                queue.append(nei)


# -----------------------------
# Driver Code (for IntelliJ run)
# -----------------------------
if __name__ == "__main__":
    # Creating graph:
    # 1 -- 2
    # |    |
    # 4 -- 3

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    print("Original Graph:")
    print_graph(node1)

    cloned = cloneGraph(node1)

    print("\nCloned Graph:")
    print_graph(cloned)


# Time Complexity: O(V + E)
# Space Complexity: O(V)
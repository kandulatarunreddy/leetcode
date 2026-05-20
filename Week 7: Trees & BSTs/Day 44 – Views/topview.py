from collections import deque


# -----------------------------
# Binary Tree Node Definition
# -----------------------------
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def topView(self, root):
        """
        Returns the Top View of Binary Tree.

        Top View:
        Nodes visible when looking at the tree from TOP.

        Example Tree:

                    1
                  /   \
                 2     3
                  \   / \
                   4 5   6

        Horizontal Distance (HD):

                  -1   0   +1
                    2   1   3
                     \ /
                      4 5
                          \
                           6 (+2)

        Top View = [2, 1, 3, 6]
        """

        # Edge case
        if not root:
            return []

        # Dictionary:
        # key = horizontal distance
        # value = first node seen at that distance
        top_nodes = {}

        # Queue stores:
        # (node, horizontal_distance)
        queue = deque([(root, 0)])

        # BFS traversal
        while queue:

            node, hd = queue.popleft()

            # ---------------------------------
            # First node at this HD
            # becomes part of top view
            # ---------------------------------
            if hd not in top_nodes:
                top_nodes[hd] = node.val

            # Add left child with hd - 1
            if node.left:
                queue.append((node.left, hd - 1))

            # Add right child with hd + 1
            if node.right:
                queue.append((node.right, hd + 1))

        # Sort by horizontal distance
        result = []

        for hd in sorted(top_nodes):
            result.append(top_nodes[hd])

        return result


# -------------------------------------------------
# Example Tree Creation
# -------------------------------------------------
#
#              1
#            /   \
#           2     3
#            \   / \
#             4 5   6
#
# Horizontal Distances:
#
#        2 (-1)
#        1 (0)
#        3 (+1)
#        6 (+2)
#
# Top View = [2, 1, 3, 6]
# -------------------------------------------------

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(4)

root.right.left = TreeNode(5)
root.right.right = TreeNode(6)


# Create solution object
solution = Solution()

# Get top view
answer = solution.topView(root)

# Print result
print("Top View of Binary Tree:", answer)


"""
------------------------------------
Dry Run
------------------------------------

Queue = [(1, 0)]

Process 1:
HD = 0

top_nodes = {0: 1}

Queue:
[(2, -1), (3, +1)]

------------------------------------

Process 2:
HD = -1

top_nodes = {
    0: 1,
   -1: 2
}

Queue:
[(3, +1), (4, 0)]

------------------------------------

Process 3:
HD = +1

top_nodes = {
    -1: 2,
     0: 1,
     1: 3
}

Queue:
[(4, 0), (5, 0), (6, 2)]

------------------------------------

Process 4:
HD = 0

Already exists → skip

Process 5:
HD = 0

Already exists → skip

Process 6:
HD = 2

top_nodes = {
    -1: 2,
     0: 1,
     1: 3,
     2: 6
}

------------------------------------

Sort by HD:

[-1, 0, 1, 2]

Result:
[2, 1, 3, 6]

------------------------------------


Time Complexity (TC):
----------------------
O(n log n)

Why?

1. BFS traversal:
O(n)

2. Sorting horizontal distances:
O(k log k)

k = unique HDs
Worst case: k = n

Total:
O(n log n)


Space Complexity (SC):
----------------------
O(n)

Why?

1. Queue for BFS
2. Dictionary for HD mapping

Worst case:
O(n)
"""
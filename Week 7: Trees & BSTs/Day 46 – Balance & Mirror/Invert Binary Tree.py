# -----------------------------
# Binary Tree Node Definition
# -----------------------------
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def invertTree(self, root):
        """
        Invert Binary Tree.

        Meaning:
        Swap left and right child
        for every node.

        Example:

                4
              /   \
             2     7
            / \   / \
           1   3 6   9

        After Invert:

                4
              /   \
             7     2
            / \   / \
           9   6 3   1
        """

        # ---------------------------------
        # Base Case:
        # Empty node
        # ---------------------------------
        if root is None:
            return None

        # ---------------------------------
        # Swap left and right child
        # ---------------------------------
        root.left, root.right = (
            root.right,
            root.left
        )

        # ---------------------------------
        # Recursively invert subtrees
        # ---------------------------------
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# -------------------------------------------------
# Helper Function:
# Print tree using level order traversal
# -------------------------------------------------
from collections import deque


def printLevelOrder(root):

    if not root:
        return

    queue = deque([root])

    while queue:

        level_size = len(queue)

        current_level = []

        for _ in range(level_size):

            node = queue.popleft()

            current_level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print(current_level)


# -------------------------------------------------
# Example Tree Creation
# -------------------------------------------------
#
# Before Invert:
#
#              4
#            /   \
#           2     7
#          / \   / \
#         1   3 6   9
#
#
# After Invert:
#
#              4
#            /   \
#           7     2
#          / \   / \
#         9   6 3   1
# -------------------------------------------------

root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Before Invert:")
printLevelOrder(root)

# Create solution object
solution = Solution()

# Invert tree
inverted_root = solution.invertTree(root)

print("\nAfter Invert:")
printLevelOrder(inverted_root)


"""
------------------------------------
DRY RUN
------------------------------------

Original Tree:

            4
          /   \
         2     7
        / \   / \
       1   3 6   9


------------------------------------
STEP 1
------------------------------------

At node 4

Swap:

2 ↔ 7

Tree becomes:

            4
          /   \
         7     2


------------------------------------
STEP 2
------------------------------------

Go left (7)

Swap:

6 ↔ 9

Subtree:

        7
       / \
      9   6


------------------------------------
STEP 3
------------------------------------

Go right (2)

Swap:

1 ↔ 3

Subtree:

        2
       / \
      3   1


------------------------------------
FINAL TREE
------------------------------------

            4
          /   \
         7     2
        / \   / \
       9   6 3   1


------------------------------------
TIME COMPLEXITY (TC)
------------------------------------

O(n)

Why?

Every node visited once.

n = number of nodes


------------------------------------
SPACE COMPLEXITY (SC)
------------------------------------

O(h)

Why?

Recursive call stack.

h = height of tree

Balanced tree:
O(log n)

Skewed tree:
O(n)
"""
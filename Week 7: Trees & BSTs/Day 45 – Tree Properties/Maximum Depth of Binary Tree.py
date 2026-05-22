# -----------------------------
# Binary Tree Node Definition
# -----------------------------
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def maxDepth(self, root):
        """
        Returns Maximum Depth of Binary Tree.

        Maximum Depth:
        Longest path from root to leaf node.

        Formula:

        depth =
        1 + max(left_depth, right_depth)
        """

        # ---------------------------------
        # Base Case:
        #
        # If node is None,
        # depth = 0
        # ---------------------------------
        if not root:
            return 0

        # Recursively find left depth
        left_depth = self.maxDepth(root.left)

        # Recursively find right depth
        right_depth = self.maxDepth(root.right)

        # ---------------------------------
        # Current depth:
        #
        # 1 for current node
        # +
        # max of left/right subtree
        # ---------------------------------
        return 1 + max(left_depth, right_depth)


# -------------------------------------------------
# Example Tree Creation
# -------------------------------------------------
#
#              1
#            /   \
#           2     3
#          /
#         4
#
# Maximum Depth:
#
# Path:
# 1 → 2 → 4
#
# Depth = 3
# -------------------------------------------------

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)

# Create solution object
solution = Solution()

# Get maximum depth
answer = solution.maxDepth(root)

# Print result
print("Maximum Depth of Binary Tree:", answer)


"""
------------------------------------
DRY RUN
------------------------------------

Tree:

        1
       / \
      2   3
     /
    4

------------------------------------

Call:
maxDepth(1)

Need:

1 + max(left, right)

------------------------------------

LEFT SUBTREE

maxDepth(2)

Need:

1 + max(left, right)

------------------------------------

LEFT SUBTREE

maxDepth(4)

Need:

1 + max(left, right)

left = None → 0
right = None → 0

depth of 4:

1 + max(0,0)
= 1

------------------------------------

RIGHT SUBTREE OF 2

None → 0

depth of 2:

1 + max(1,0)
= 2

------------------------------------

RIGHT SUBTREE OF 1

maxDepth(3)

left = None → 0
right = None → 0

depth of 3:

1 + max(0,0)
= 1

------------------------------------

depth of 1:

1 + max(2,1)
= 3

------------------------------------

FINAL ANSWER

3


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
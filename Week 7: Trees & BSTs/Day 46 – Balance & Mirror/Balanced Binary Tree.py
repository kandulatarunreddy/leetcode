# -----------------------------
# Binary Tree Node Definition
# -----------------------------
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def isBalanced(self, root):
        """
        Returns True if tree is balanced.

        Balanced Tree:
        Difference between left and right
        subtree height <= 1
        """

        def dfs(node):

            # ---------------------------------
            # Base case
            #
            # Empty tree height = 0
            # ---------------------------------
            if not node:
                return 0

            # Height of left subtree
            left_height = dfs(node.left)

            # ---------------------------------
            # If left subtree already
            # unbalanced → stop
            # ---------------------------------
            if left_height == -1:
                return -1

            # Height of right subtree
            right_height = dfs(node.right)

            # ---------------------------------
            # If right subtree already
            # unbalanced → stop
            # ---------------------------------
            if right_height == -1:
                return -1

            # ---------------------------------
            # Check balance condition
            #
            # abs(left - right) <= 1
            # ---------------------------------
            if abs(left_height - right_height) > 1:
                return -1

            # ---------------------------------
            # Return height of current node
            #
            # 1 + max(left, right)
            # ---------------------------------
            return 1 + max(
                left_height,
                right_height
            )

        # If result is -1 → unbalanced
        return dfs(root) != -1


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
# Balanced:
#
# Node 2:
# |1 - 0| = 1
#
# Node 1:
# |2 - 1| = 1
#
# Result = True
# -------------------------------------------------

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)

# Create solution object
solution = Solution()

# Check if balanced
answer = solution.isBalanced(root)

# Print result
print("Is Balanced Binary Tree:", answer)


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

Node 4

left = 0
right = 0

difference:

|0 - 0| = 0

Balanced

height = 1


------------------------------------

Node 2

left = 1
right = 0

difference:

|1 - 0| = 1

Balanced

height:

1 + max(1,0)
= 2


------------------------------------

Node 3

height = 1


------------------------------------

Node 1

left = 2
right = 1

difference:

|2 - 1| = 1

Balanced

height:

1 + max(2,1)
= 3


------------------------------------

FINAL ANSWER

True


------------------------------------
UNBALANCED EXAMPLE
------------------------------------

        1
       /
      2
     /
    3

Node 1:

left = 2
right = 0

difference:

|2 - 0| = 2

NOT BALANCED

returns -1


------------------------------------
TIME COMPLEXITY (TC)
------------------------------------

O(n)

Why?

Every node visited once.


------------------------------------
SPACE COMPLEXITY (SC)
------------------------------------

O(h)

Why?

Recursive stack space.

h = tree height

Balanced tree:
O(log n)

Skewed tree:
O(n)
"""
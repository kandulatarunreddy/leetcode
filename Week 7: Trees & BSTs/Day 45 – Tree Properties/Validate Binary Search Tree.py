# -----------------------------
# Binary Tree Node Definition
# -----------------------------
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def isValidBST(self, root):
        """
        Validate Binary Search Tree.

        BST Rule:
        left subtree < node < right subtree

        Every node must stay within
        a valid min/max range.
        """

        def dfs(node, minimum, maximum):

            # ---------------------------------
            # Base case
            #
            # Empty node is valid
            # ---------------------------------
            if not node:
                return True

            # ---------------------------------
            # Check BST condition
            #
            # Node must be:
            #
            # minimum < node.val < maximum
            # ---------------------------------
            if not (minimum < node.val < maximum):
                return False

            # Validate left subtree
            left_valid = dfs(node.left,minimum,node.val)

            # Validate right subtree
            right_valid = dfs(node.right,node.val,maximum)

            return left_valid and right_valid

        # Start with infinite range
        return dfs(root,float('-inf'),float('inf'))


# -------------------------------------------------
# Example 1: Valid BST
# -------------------------------------------------
#
#              5
#            /   \
#           3     8
#          / \
#         2   4
#
# Valid BST
# -------------------------------------------------

root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(8)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

# Create solution object
solution = Solution()

# Validate BST
answer = solution.isValidBST(root)

# Print result
print("Is Valid BST:", answer)


"""
------------------------------------
DRY RUN
------------------------------------

Tree:

        5
       / \
      3   8
     / \
    2   4

------------------------------------

Start:

dfs(5, -∞, +∞)

Check:

-∞ < 5 < +∞

VALID

------------------------------------

LEFT SUBTREE

dfs(3, -∞, 5)

Check:

-∞ < 3 < 5

VALID

------------------------------------

LEFT OF 3

dfs(2, -∞, 3)

Check:

-∞ < 2 < 3

VALID


------------------------------------

RIGHT OF 3

dfs(4, 3, 5)

Check:

3 < 4 < 5

VALID


------------------------------------

RIGHT SUBTREE

dfs(8, 5, +∞)

Check:

5 < 8 < +∞

VALID


------------------------------------

FINAL ANSWER

True


------------------------------------
INVALID EXAMPLE
------------------------------------

        5
       / \
      1   4
         / \
        3   6

Node 3 fails:

Should be > 5
because it is inside right subtree of 5

But:

3 < 5

INVALID BST


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
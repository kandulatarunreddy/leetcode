# -----------------------------
# Binary Tree Node Definition
# -----------------------------
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def isSymmetric(self, root):
        """
        Check if Binary Tree is Symmetric.

        Symmetric Tree:
        Left subtree should be mirror image
        of right subtree.

        Example:

                  1
                /   \
               2     2
              / \   / \
             3   4 4   3

        Symmetric = True
        """

        # ---------------------------------
        # Helper function:
        # Check if two trees are mirror
        # images of each other
        # ---------------------------------
        def isMirror(left_tree, right_tree):

            # -----------------------------
            # Case 1:
            # Both nodes are None
            #
            # Mirror match
            # -----------------------------
            if left_tree is None and right_tree is None:
                return True

            # -----------------------------
            # Case 2:
            # One node missing
            #
            # Not symmetric
            # -----------------------------
            if left_tree is None or right_tree is None:
                return False

            # -----------------------------
            # Case 3:
            # Values must match
            # -----------------------------
            if left_tree.val != right_tree.val:
                return False

            # -----------------------------
            # Mirror comparison:
            #
            # left.left  ↔ right.right
            # left.right ↔ right.left
            # -----------------------------
            outside_match = isMirror(left_tree.left,right_tree.right)

            inside_match = isMirror(left_tree.right,right_tree.left)

            return outside_match and inside_match

        # Empty tree is symmetric
        if not root:
            return True

        # Compare left and right subtree
        return isMirror(root.left,root.right)


# -------------------------------------------------
# Example Tree Creation
# -------------------------------------------------
#
#               1
#             /   \
#            2     2
#           / \   / \
#          3   4 4   3
#
# Symmetric = True
# -------------------------------------------------

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

# Create solution object
solution = Solution()

# Check symmetry
answer = solution.isSymmetric(root)

# Print result
print("Is Symmetric Tree?:", answer)


"""
------------------------------------
DRY RUN
------------------------------------

Tree:

            1
          /   \
         2     2
        / \   / \
       3   4 4   3


------------------------------------
STEP 1
------------------------------------

Compare:

root.left vs root.right

2 == 2

Continue


------------------------------------
STEP 2
------------------------------------

Mirror comparison:

left.left ↔ right.right

3 ↔ 3

MATCH


------------------------------------
STEP 3
------------------------------------

left.right ↔ right.left

4 ↔ 4

MATCH


------------------------------------
STEP 4
------------------------------------

Children of leaf nodes:

None ↔ None

True


------------------------------------
FINAL RESULT
------------------------------------

All mirror checks passed

True


------------------------------------
NOT SYMMETRIC EXAMPLE
------------------------------------

            1
          /   \
         2     2
          \     \
           3     3

Wrong mirror structure.

Expected:

left.right ↔ right.left

But got:

left.right ↔ right.right

Result = False


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

h = height of tree

Balanced tree:
O(log n)

Skewed tree:
O(n)
"""
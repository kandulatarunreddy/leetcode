# -----------------------------
# Binary Tree Node Definition
# -----------------------------
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def isSameTree(self, p, q):
        """
        Check whether two binary trees
        are exactly the same.

        Same Tree means:
        1. Same structure
        2. Same node values
        """

        # ---------------------------------
        # Case 1:
        # Both nodes are None
        #
        # Example:
        #
        # None    None
        #
        # Same
        # ---------------------------------
        if p is None and q is None:
            return True

        # ---------------------------------
        # Case 2:
        # Both nodes exist
        # AND values match
        #
        # Continue checking children
        # ---------------------------------
        if p and q and p.val == q.val:

            # Left subtree must match
            left_same = self.isSameTree(p.left,q.left)

            # Right subtree must match
            right_same = self.isSameTree(p.right,q.right)

            return left_same and right_same

        # ---------------------------------
        # Case 3:
        #
        # One node missing OR
        # Values different
        #
        # NOT same tree
        # ---------------------------------
        return False


# -------------------------------------------------
# Example Tree Creation
# -------------------------------------------------
#
# Tree 1:
#
#            1
#          /   \
#         2     3
#
#
# Tree 2:
#
#            1
#          /   \
#         2     3
#
# Same Tree = True
# -------------------------------------------------

# -----------------------------
# Create Tree 1
# -----------------------------
p = TreeNode(1)

p.left = TreeNode(2)
p.right = TreeNode(3)

# -----------------------------
# Create Tree 2
# -----------------------------
q = TreeNode(1)

q.left = TreeNode(2)
q.right = TreeNode(3)

# Create solution object
solution = Solution()

# Check if trees are same
answer = solution.isSameTree(p, q)

# Print result
print("Are Both Trees Same?:", answer)


"""
------------------------------------
DRY RUN
------------------------------------

Tree 1:          Tree 2:

      1                1
     / \              / \
    2   3            2   3


------------------------------------
STEP 1
------------------------------------

Compare root:

1 == 1

Values match

Continue recursion


------------------------------------
STEP 2
------------------------------------

Compare left child:

2 == 2

Values match

Compare children:

left:
None == None

True

right:
None == None

True

Result for node 2:

True AND True
= True


------------------------------------
STEP 3
------------------------------------

Compare right child:

3 == 3

Values match

Compare children:

left:
None == None

True

right:
None == None

True

Result for node 3:

True


------------------------------------
FINAL RESULT
------------------------------------

left_same AND right_same

True AND True

= True


------------------------------------
OUTPUT
------------------------------------

Are Both Trees Same?: True


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

Recursive stack space.

h = height of tree

Balanced tree:
O(log n)

Skewed tree:
O(n)
"""
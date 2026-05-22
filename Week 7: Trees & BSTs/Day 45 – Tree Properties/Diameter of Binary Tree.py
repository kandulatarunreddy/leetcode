# -----------------------------
# Binary Tree Node Definition
# -----------------------------
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def diameterOfBinaryTree(self, root):
        """
        Returns Diameter of Binary Tree.

        Diameter:
        Longest path between any two nodes.

        Measured in number of EDGES.
        """

        # Store maximum diameter found
        self.max_diameter = 0

        def dfs(node):

            # ---------------------------------
            # Base case
            #
            # Null node height = 0
            # ---------------------------------
            if not node:
                return 0

            # Height of left subtree
            left_height = dfs(node.left)

            # Height of right subtree
            right_height = dfs(node.right)

            # ---------------------------------
            # Diameter passing through
            # current node
            #
            # left subtree depth
            # +
            # right subtree depth
            # ---------------------------------
            current_diameter = (left_height + right_height)

            # Update global maximum
            self.max_diameter = max(self.max_diameter,current_diameter)

            # ---------------------------------
            # Return height of current node
            #
            # 1 + max(left, right)
            # ---------------------------------
            return 1 + max(left_height,right_height)

        # Run DFS
        dfs(root)

        return self.max_diameter


# -------------------------------------------------
# Example Tree Creation
# -------------------------------------------------
#
#              1
#            /   \
#           2     3
#          / \
#         4   5
#
# Longest Path:
#
# 4 → 2 → 1 → 3
#
# Diameter = 3 edges
# -------------------------------------------------

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Create solution object
solution = Solution()

# Get diameter
answer = solution.diameterOfBinaryTree(root)

# Print result
print("Diameter of Binary Tree:", answer)


"""
------------------------------------
DRY RUN
------------------------------------

Tree:

        1
       / \
      2   3
     / \
    4   5

------------------------------------

Node 4

left = 0
right = 0

diameter = 0

height = 1


------------------------------------

Node 5

left = 0
right = 0

diameter = 0

height = 1


------------------------------------

Node 2

left_height = 1
right_height = 1

diameter through 2:

1 + 1 = 2

max_diameter = 2

height of 2:

1 + max(1,1)
= 2


------------------------------------

Node 3

height = 1


------------------------------------

Node 1

left_height = 2
right_height = 1

diameter through 1:

2 + 1 = 3

max_diameter = 3


------------------------------------

FINAL ANSWER

3

Longest path:

4 → 2 → 1 → 3


------------------------------------
TIME COMPLEXITY (TC)
------------------------------------

O(n)

Why?

Every node visited exactly once.


------------------------------------
SPACE COMPLEXITY (SC)
------------------------------------

O(h)

Why?

Recursive call stack.

h = tree height

Balanced tree:
O(log n)

Skewed tree:
O(n)
"""
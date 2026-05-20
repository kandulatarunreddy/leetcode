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
    def leftView(self, root):
        """
        Returns the left view of a binary tree.

        Left View:
        Nodes visible when looking at the tree from the LEFT side.

        Example:
                    1
                  /   \
                 2     3
                / \     \
               4   5     6

        Left View = [1, 2, 4]
        """

        # Edge case: empty tree
        if not root:
            return []

        result = []

        # Queue for BFS (Level Order Traversal)
        queue = deque([root])

        # Process tree level by level
        while queue:

            # Number of nodes at current level
            level_size = len(queue)

            # Traverse every node in this level
            for i in range(level_size):

                # Get current node
                node = queue.popleft()

                # ---------------------------------
                # Left view logic:
                # First node of every level
                # is visible from left side
                # ---------------------------------
                if i == 0:
                    result.append(node.val)

                # ---------------------------------
                # IMPORTANT:
                # We STILL process all nodes
                # because their children are needed
                # for the next level.
                # ---------------------------------

                # Add left child
                if node.left:
                    queue.append(node.left)

                # Add right child
                if node.right:
                    queue.append(node.right)

        return result


# -------------------------------------------------
# Example Tree Creation
# -------------------------------------------------
#
#             1
#           /   \
#          2     3
#         / \     \
#        4   5     6
#
# Left View:
# Level 0 -> [1]       => 1
# Level 1 -> [2, 3]    => 2
# Level 2 -> [4, 5, 6] => 4
#
# Output = [1, 2, 4]
# -------------------------------------------------

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.right = TreeNode(6)


# Create solution object
solution = Solution()

# Get left view
answer = solution.leftView(root)

# Print result
print("Left View of Binary Tree:", answer)


"""
------------------------------------
Dry Run
------------------------------------

Queue = [1]

Level 0:
Process 1
i == 0 → add 1
Queue becomes [2, 3]

Result = [1]

------------------------------------

Level 1:
Process 2
i == 0 → add 2

Process 3

Queue becomes [4, 5, 6]

Result = [1, 2]

------------------------------------

Level 2:
Process 4
i == 0 → add 4

Process 5
Process 6

Result = [1, 2, 4]

------------------------------------
Final Output:
[1, 2, 4]
------------------------------------


Time Complexity (TC):
----------------------
O(n)

Reason:
Every node is visited exactly once.

n = number of nodes


Space Complexity (SC):
----------------------
O(w)

Reason:
Queue stores nodes level-by-level.

w = maximum width of the tree

Worst case:
O(n)
(for a complete binary tree)
"""
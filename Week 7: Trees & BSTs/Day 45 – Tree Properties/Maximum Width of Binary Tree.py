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

    def widthOfBinaryTree(self, root):
        """
        Find Maximum Width of Binary Tree.

        Width:
        Number of positions between leftmost and
        rightmost non-null nodes INCLUDING gaps.

        Example:

                    1
                  /   \
                 3     2
                /       \
               5         9
              /           \
             6             7

        Widths:

        Level 0 -> [1]
        Width = 1

        Level 1 -> [3, 2]
        Width = 2

        Level 2 -> [5, null, null, 9]
        Width = 4

        Level 3 -> [6, null, null, null,
                    null, null, null, 7]
        Width = 8

        Maximum Width = 8
        """

        # Edge case:
        # Empty tree
        if not root:
            return 0

        # Store maximum width found
        max_width = 0

        # Queue stores:
        # (node, index)
        #
        # Indexing like Complete Binary Tree:
        #
        # Root = 0
        # Left child = 2*i + 1
        # Right child = 2*i + 2
        #
        queue = deque([(root, 0)])

        # BFS traversal
        while queue:

            # Number of nodes in current level
            level_size = len(queue)

            # ---------------------------------
            # Leftmost index of current level
            #
            # Used for normalization
            #
            # Why normalize?
            #
            # Deep trees create huge indices:
            #
            # 0, 2, 6, 14, 30, 62...
            #
            # So we shift current level
            # to start from 0.
            #
            # This keeps numbers small
            # and avoids overflow issues.
            # ---------------------------------
            min_index = queue[0][1]

            # Process ALL nodes
            # in current level
            for i in range(level_size):

                node, index = queue.popleft()

                # -----------------------------
                # Normalize index
                #
                # Example:
                #
                # Original:
                # [7, 14]
                #
                # Normalized:
                # [0, 7]
                #
                # Width remains same:
                #
                # 14 - 7 + 1 = 8
                # 7 - 0 + 1 = 8
                # -----------------------------
                current_index = index - min_index

                # First node of level
                if i == 0:
                    left_most = current_index

                # Last node of level
                if i == level_size - 1:
                    right_most = current_index

                # Add left child
                if node.left:
                    queue.append((node.left,2 * current_index + 1))

                # Add right child
                if node.right:
                    queue.append((node.right,2 * current_index + 2))

            # ---------------------------------
            # Calculate current level width
            #
            # Formula:
            #
            # right - left + 1
            # ---------------------------------
            current_width = (right_most - left_most + 1)

            # Update answer
            max_width = max(max_width,current_width)

        return max_width


# -------------------------------------------------
# Example Tree Creation
# -------------------------------------------------
#
#              1
#            /   \
#           3     2
#          /       \
#         5         9
#        /           \
#       6             7
#
# Level 0:
# [1]
# Width = 1
#
# Level 1:
# [3, 2]
# Width = 2
#
# Level 2:
# [5, null, null, 9]
# Width = 4
#
# Level 3:
# [6, null, null, null,
#  null, null, null, 7]
#
# Width = 8
#
# Maximum Width = 8
# -------------------------------------------------

root = TreeNode(1)

root.left = TreeNode(3)
root.right = TreeNode(2)

root.left.left = TreeNode(5)
root.right.right = TreeNode(9)

root.left.left.left = TreeNode(6)
root.right.right.right = TreeNode(7)

# Create solution object
solution = Solution()

# Get answer
answer = solution.widthOfBinaryTree(root)

# Print result
print(
    "Maximum Width of Binary Tree:",
    answer
)


"""
------------------------------------
DRY RUN
------------------------------------

Queue:
[(1, 0)]


------------------------------------
LEVEL 0
------------------------------------

level_size = 1

min_index = 0

Process node 1:

normalized index:
0 - 0 = 0

left_most = 0
right_most = 0

Add children:

3 -> index 1
2 -> index 2

Queue:
[(3,1), (2,2)]

Width:
0 - 0 + 1 = 1

max_width = 1


------------------------------------
LEVEL 1
------------------------------------

Queue:
[(3,1), (2,2)]

min_index = 1

Process 3:

normalized:
1 - 1 = 0

left_most = 0

Add:
5 -> index 1

Process 2:

normalized:
2 - 1 = 1

right_most = 1

Add:
9 -> index 4

Width:
1 - 0 + 1 = 2

max_width = 2


------------------------------------
LEVEL 2
------------------------------------

Queue:
[(5,1), (9,4)]

min_index = 1

Process 5:

normalized:
1 - 1 = 0

left_most = 0

Add:
6 -> index 1

Process 9:

normalized:
4 - 1 = 3

right_most = 3

Add:
7 -> index 8

Width:
3 - 0 + 1 = 4

max_width = 4


------------------------------------
LEVEL 3
------------------------------------

Queue:
[(6,1), (7,8)]

min_index = 1

Process 6:

normalized:
1 - 1 = 0

left_most = 0

Process 7:

normalized:
8 - 1 = 7

right_most = 7

Width:
7 - 0 + 1 = 8

max_width = 8


------------------------------------
FINAL ANSWER
------------------------------------

8

------------------------------------
TIME COMPLEXITY (TC)
------------------------------------

O(n)

Why?

Every node is visited once.

n = number of nodes


------------------------------------
SPACE COMPLEXITY (SC)
------------------------------------

O(n)

Why?

Queue stores nodes level-by-level.

Worst case:
Complete binary tree
"""
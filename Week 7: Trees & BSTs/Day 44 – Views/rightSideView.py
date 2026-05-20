from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case: empty tree
        if not root:
            return []

        result = []
        queue = deque([root])  # BFS queue

        # Process tree level by level
        while queue:
            level_size = len(queue)

            # Traverse all nodes at current level
            for i in range(level_size):
                node = queue.popleft()

                # The last node in this level
                # is visible from the right side
                if i == level_size - 1:
                    result.append(node.val)

                # Add children for next level
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result

'''Time Complexity (TC)
O(n) → Every node is visited exactly once.
Space Complexity (SC)
O(w) → Queue stores at most one level of nodes.
w = maximum width of the tree
Worst case: O(n)
'''
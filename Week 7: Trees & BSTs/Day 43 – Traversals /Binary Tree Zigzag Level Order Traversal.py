from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def zigzagLevelOrder(root):
    """
    TC: O(n) → each node visited once
    SC: O(n) → queue + result storage
    """

    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        size = len(queue)
        level = deque()  # efficient insert at both ends

        for _ in range(size):
            node = queue.popleft()

            # If left → right: append at end
            # If right → left: append at front
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            # add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level))
        left_to_right = not left_to_right  # flip direction

    return result

# -------------------------
# DRIVER CODE
# -------------------------
if __name__ == "__main__":

    """
            3
           / \
          9  20
             / \
            15  7

    Expected Output:
    [[3], [20, 9], [15, 7]]
    """

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(zigzagLevelOrder(root))
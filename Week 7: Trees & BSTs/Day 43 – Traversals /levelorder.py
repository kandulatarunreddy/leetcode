from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# =========================
# 1. BFS APPROACH (QUEUE)
# =========================
def levelOrderBFS(root):
    """
    Time Complexity (TC): O(n)
    Space Complexity (SC): O(n)
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# =========================
# 2. DFS APPROACH (RECURSION)
# =========================
def levelOrderDFS(root):
    """
    Time Complexity (TC): O(n)
    Space Complexity (SC):
        - O(h) recursion stack (h = height of tree)
        - O(n) for output storage
    """
    result = []

    def dfs(node, depth):
        if not node:
            return

        # create new level if needed
        if len(result) == depth:
            result.append([])

        result[depth].append(node.val)

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return result


# =========================
# DRIVER CODE
# =========================
if __name__ == "__main__":
    """
            3
           / \
          9  20
             / \
            15  7
    """

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("BFS Level Order:", levelOrderBFS(root))
    print("DFS Level Order:", levelOrderDFS(root))
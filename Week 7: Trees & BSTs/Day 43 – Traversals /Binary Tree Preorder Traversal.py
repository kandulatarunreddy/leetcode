# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def preorderTraversal(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        current = stack.pop()
        result.append(current.val)

        # Push right first, then left
        # So left gets processed first
        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return result


# Driver Code
if __name__ == "__main__":
    """
          1
           \
            2
           /
          3

    Preorder Traversal: [1, 2, 3]
    """

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print("Preorder Traversal:", preorderTraversal(root))


"""
Time Complexity (TC): O(n)
- Visit every node exactly once.

Space Complexity (SC): O(n)
- Worst case (skewed tree), stack stores all nodes.
"""
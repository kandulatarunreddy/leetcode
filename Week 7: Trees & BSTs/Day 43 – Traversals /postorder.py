# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def postorderTraversal(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        current = stack.pop()

        # Add root first
        result.append(current.val)

        # Push left first, then right
        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    # Reverse to get Left -> Right -> Root
    return result[::-1]


# Driver Code
if __name__ == "__main__":
    """
          1
           \
            2
           /
          3

    Postorder Traversal: [3, 2, 1]
    """

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = newNode = TreeNode(3)

    print("Postorder Traversal:", postorderTraversal(root))


"""
Time Complexity (TC): O(n)
- Visit every node once.

Space Complexity (SC): O(n)
- Stack + output array in worst case.
"""
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def inorderTraversal(root):
    result = []
    stack = []
    current = root

    while current or stack:

        # Traverse to the leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Process node
        current = stack.pop()
        result.append(current.val)

        # Move to right subtree
        current = current.right

    return result

def inorderTraversal1(root):
    result = []

    def inorder(node):
        if not node:
            return

        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result



# Driver Code
if __name__ == "__main__":
    """
          1
           \
            2
           /
          3

    Inorder Traversal: [1, 3, 2]
    """

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    result = inorderTraversal(root)

    print("Inorder Traversal:", result)


"""
Time Complexity (TC): O(n)
- Each node is pushed and popped from stack exactly once.

Space Complexity (SC): O(n)
- Worst case (skewed tree), stack stores all nodes.
"""

"""
Time Complexity (TC): O(n)

Space Complexity (SC): O(h)
- h = height of tree
- O(log n) for balanced tree
- O(n) for skewed tree
"""
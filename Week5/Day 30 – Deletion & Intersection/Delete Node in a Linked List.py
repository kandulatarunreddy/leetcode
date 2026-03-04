# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Delete the given node (not the last node).
        Modify in-place.
        """
        # Copy value from next node
        node.val = node.next.val

        # Skip the next node
        node.next = node.next.next


# Helper function to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# ----------- TEST CASE -----------

# Create linked list: 4 -> 5 -> 1 -> 9
head = ListNode(4)
node_to_delete = ListNode(5)
head.next = node_to_delete
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

print("Original List:")
print_list(head)

# Delete node with value 5
solution = Solution()
solution.deleteNode(node_to_delete)

print("After Deleting Node:")
print_list(head)

# Time Complexity: O(1)
# Space Complexity: O(1)
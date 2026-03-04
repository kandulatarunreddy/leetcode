from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Dummy node to handle edge cases (like removing the head)
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from end
        slow.next = slow.next.next

        return dummy.next


# Helper function to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# ----------- TEST CASE -----------

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2  # Remove 2nd node from end

solution = Solution()
new_head = solution.removeNthFromEnd(head, n)

print("Updated List:")
print_list(new_head)

# Time Complexity: O(n)
# Space Complexity: O(1)
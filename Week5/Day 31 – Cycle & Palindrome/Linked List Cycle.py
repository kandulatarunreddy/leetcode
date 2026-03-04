from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# ----------------------------
# Helper function to create linked list
# ----------------------------
def create_linked_list(values, pos):
    """
    values = list of node values
    pos = index where tail connects (0-based)
          -1 means no cycle
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    if pos == 0:
        cycle_node = head

    for i in range(1, len(values)):
        new_node = ListNode(values[i])
        current.next = new_node
        current = new_node

        if i == pos:
            cycle_node = new_node

    if pos != -1:
        current.next = cycle_node

    return head


# ----------------------------
# Test Cases
# ----------------------------

sol = Solution()

# Test Case 1: No Cycle
head1 = create_linked_list([1, 2, 3, 4], -1)
print("Test Case 1 (No Cycle):", sol.hasCycle(head1))  # Expected: False

# Test Case 2: With Cycle (tail connects to index 1)
head2 = create_linked_list([10, 20, 30, 40], 1)
print("Test Case 2 (With Cycle):", sol.hasCycle(head2))  # Expected: True


# TC: O(N)
# SC: O(1)
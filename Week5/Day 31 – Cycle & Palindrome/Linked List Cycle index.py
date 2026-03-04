from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycleIndex(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return -1   # No cycle

        # Step 2: Find starting node of cycle
        slow = head
        index = 0

        while slow != fast:
            slow = slow.next
            fast = fast.next
            index += 1

        return index


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
# Test Case
# ----------------------------

sol = Solution()

# Example:
# head = [3,2,0,-4], pos = 1
head = create_linked_list([3, 2, 0, -4], 1)

result = sol.detectCycleIndex(head)

print("Cycle starts at index:", result)


# TC: O(N)
# SC: O(1)
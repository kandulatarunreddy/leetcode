from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# ----------------------------
# Helper Function
# ----------------------------
def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


# ----------------------------
# Test Cases
# ----------------------------

sol = Solution()

# Test Case 1
head1 = create_linked_list([1, 2, 2, 1])
print("Is Palindrome:", sol.isPalindrome(head1))  # Expected: True

# Test Case 2
head2 = create_linked_list([1, 2])
print("Is Palindrome:", sol.isPalindrome(head2))  # Expected: False


# TC: O(N)
# SC: O(1)
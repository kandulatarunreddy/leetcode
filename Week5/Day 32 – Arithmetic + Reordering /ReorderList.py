from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # =====================================================
        # STEP 1: FIND MIDDLE
        # =====================================================

        slow = head
        fast = head

        # INITIAL:
        # FULL LIST:
        # 1 → 2 → 3 → 4 → 5 → None
        #
        # slow = 1 → 2 → 3 → 4 → 5
        # fast = 1 → 2 → 3 → 4 → 5

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # AFTER LOOP:
        #
        # slow = 3 → 4 → 5
        # fast = None
        #
        # FULL LIST STILL UNCHANGED:
        # 1 → 2 → 3 → 4 → 5

        # =====================================================
        # STEP 2: REVERSE SECOND HALF
        # =====================================================

        prev = None
        curr = slow.next

        # BREAK THE LIST
        slow.next = None

        # NOW WE HAVE TWO SEPARATE LISTS:
        #
        # FIRST HALF:
        # 1 → 2 → 3 → None
        #
        # SECOND HALF:
        # 4 → 5 → None
        #
        # prev = None
        # curr = 4

        while curr:
            nxt = curr.next

            # Example first iteration:
            # curr = 4
            # nxt = 5

            curr.next = prev
            # 4 → None

            prev = curr
            # prev = 4

            curr = nxt
            # curr = 5

        # After reversal finishes:

        # prev = 5 → 4 → None
        # curr = None
        # nxt = last stored value (None)

        # NOW STRUCTURE IS:

        # First Half:
        # 1 → 2 → 3 → None
        #
        # Second Half (Reversed):
        # 5 → 4 → None

        # =====================================================
        # STEP 3: MERGE BOTH HALVES
        # =====================================================

        first = head
        second = prev

        # BEFORE MERGE:
        #
        # first  = 1 → 2 → 3 → None
        # second = 5 → 4 → None

        while second:

            tmp1 = first.next   # next node in first half
            tmp2 = second.next  # next node in second half

            # LINK first → second
            first.next = second
            # Now:
            # 1 → 5

            # LINK second → tmp1
            second.next = tmp1
            # Now:
            # 1 → 5 → 2

            # MOVE POINTERS
            first = tmp1
            second = tmp2

        # =====================================================
        # FINAL RESULT
        # =====================================================

        # FULL FINAL LIST:
        # 1 → 5 → 2 → 4 → 3 → None
        #
        # POINTER STATES AFTER COMPLETION:
        #
        # head  → 1 (start of reordered list)
        # first → 3
        # second → None
        # slow  → 3
        # prev  → 5
        # curr  → None
        # nxt   → None


# Helper functions for testing
def create_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Main
if __name__ == "__main__":
    head = create_list([1, 2, 3, 4, 5])

    Solution().reorderList(head)

    print_list(head)


# Time Complexity: O(n)
# Space Complexity: O(1)
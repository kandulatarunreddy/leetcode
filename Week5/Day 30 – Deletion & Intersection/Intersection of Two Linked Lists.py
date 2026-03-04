from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
            self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        if not headA or not headB:
            return None

        p1 = headA
        p2 = headB

        while p1 != p2:
            '''
            List A: 4 → 1 → 8 → 4 → 5      (length 5)
            List B: 5 → 6 → 1 → 8 → 4 → 5  (length 6)
            p1 path: 4 → 1 → 8 → 4 → 5 → null → 5 → 6 → 1 → 8
            p2 path: 5 → 6 → 1 → 8 → 4 → 5 → null → 4 → 1 → 8
            '''

            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        # Either both are None (no intersection),
        # or both meet at intersection node.
        return p1



# ----------------------------
# Example Test Case
# ----------------------------

# Creating intersection manually:
# A: 1 -> 2
#              \
#               8 -> 9
#              /
# B:     3 -> 4

# Common part
common = ListNode(8)
common.next = ListNode(9)

# List A
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = common

# List B
headB = ListNode(3)
headB.next = ListNode(4)
headB.next.next = common

# Run
sol = Solution()
result = sol.getIntersectionNode(headA, headB)

if result:
    print("Intersection at node with value:", result.val)
else:
    print("No intersection")


# TC: O(N + M)
# SC: O(1)
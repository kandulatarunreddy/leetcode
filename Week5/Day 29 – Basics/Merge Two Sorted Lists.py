from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)  # Temporary dummy node
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Attach remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next


# Helper function to print list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Example Test
# list1: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# list2: 1 -> 3 -> 5
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(5)

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

print("Merged List:")
print_list(merged)

# TC: O(n + m), SC: O(1)
# - We only use a constant number of pointers.
# - Dummy node is a fixed-size object.
# - We do NOT create new nodes for each element.
# - Extra memory does not grow with input size.
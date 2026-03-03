from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next   # store next
            current.next = prev       # reverse pointer
            prev = current            # move prev forward
            current = next_node       # move current forward

        return prev


# 🔹 Helper function to print linked list
def print_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# 🔹 Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original List:")
print_list(head)

# 🔹 Reverse the list
solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed List:")
print_list(reversed_head)

#Tc: O(n) Sc: O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and last node
        cur, n = head, 1
        while cur.next:
            n += 1
            cur = cur.next

        # Step 2: Make it circular
        cur.next = head

        # Step 3: Reduce k
        k %= n

        # Step 4: Move to new tail
        for i in range(n - k):
            cur = cur.next

        # Step 5: Break the circle
        head = cur.next
        cur.next = None

        return head


# Helper function to create linked list
def create_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# Helper function to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Main execution
if __name__ == "__main__":
    # Example input
    head = create_list([1, 2, 3, 4, 5])
    k = 2

    solution = Solution()
    new_head = solution.rotateRight(head, k)

    print("Rotated List:")
    print_list(new_head)
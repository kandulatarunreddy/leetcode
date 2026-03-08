from typing import Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # If list is empty OR left == right, nothing to reverse
        if not head or left == right:
            return head

        # Dummy node helps handle edge cases (like reversing from head)
        dummy = ListNode(0)
        dummy.next = head

        # prev will eventually point to node BEFORE the 'left' position
        prev = dummy

        # Move prev to the node just before the left position
        for _ in range(left - 1):
            prev = prev.next

        # curr will point to the first node of the sublist to reverse
        curr = prev.next

        # Reverse the sublist using head-insertion technique
        for _ in range(right - left):

            # temp is the node that will be moved to the front
            temp = curr.next

            # Remove temp from its current position
            curr.next = temp.next

            # Insert temp right after prev
            temp.next = prev.next
            prev.next = temp

        return dummy.next


# -------- Helper Functions --------

# Build linked list from Python list
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


# Print linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# -------- Main Execution --------

if __name__ == "__main__":

    # Example list
    arr = [1, 2, 3, 4, 5]

    # Build linked list
    head = build_list(arr)

    print("Original List:")
    print_list(head)

    sol = Solution()

    # Reverse from position 2 to 4
    new_head = sol.reverseBetween(head, 2, 4)

    print("\nAfter Reversing from 2 to 4:")
    print_list(new_head)
# Time Complexity: O(n)
# Space Complexity: O(1)
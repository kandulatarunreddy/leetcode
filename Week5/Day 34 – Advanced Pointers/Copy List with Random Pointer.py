from typing import Optional


# Definition for a Node
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        # Dictionary to store mapping of original node -> copied node
        oldToCopy = {None: None}

        # ---------------------------
        # Pass 1: Create copy of nodes
        # ---------------------------
        cur = head
        while cur:
            copy = Node(cur.val)       # create new node with same value
            oldToCopy[cur] = copy      # store mapping
            cur = cur.next

        # --------------------------------
        # Pass 2: Assign next and random
        # --------------------------------
        cur = head
        while cur:
            copy = oldToCopy[cur]

            # connect next pointer
            copy.next = oldToCopy[cur.next]

            # connect random pointer
            copy.random = oldToCopy[cur.random]

            cur = cur.next

        # return head of copied list
        return oldToCopy[head]


# -------------------------------------
# Helper function to print linked list
# -------------------------------------
def print_list(head):
    cur = head
    while cur:
        rand = cur.random.val if cur.random else None
        print(f"Node({cur.val}) -> Random({rand})")
        cur = cur.next
    print()


# -------------------------------------
# Main function to test in IntelliJ
# -------------------------------------
if __name__ == "__main__":

    # Create nodes
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    # Connect next pointers
    n1.next = n2
    n2.next = n3

    # Connect random pointers
    n1.random = n3
    n2.random = n1
    n3.random = None

    print("Original List:")
    print_list(n1)

    sol = Solution()
    copied_head = sol.copyRandomList(n1)

    print("Copied List:")
    print_list(copied_head)


# Time Complexity: O(n)
# Space Complexity: O(n)
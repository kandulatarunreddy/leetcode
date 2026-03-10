from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        if not head:
            return None

        cur = head

        # -----------------------------------
        # Step 1: Insert copied nodes
        # A -> B -> C
        # becomes
        # A -> A' -> B -> B' -> C -> C'
        # -----------------------------------
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next

        cur = head

        # -----------------------------------
        # Step 2: Assign random pointers
        # -----------------------------------
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        copy_head = head.next

        # -----------------------------------
        # Step 3: Separate the two lists
        # -----------------------------------
        while cur:
            copy = cur.next
            cur.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            cur = cur.next

        return copy_head


# -----------------------------
# Helper function to print list
# -----------------------------
def print_list(head):
    cur = head
    while cur:
        rand = cur.random.val if cur.random else None
        print(f"Node({cur.val}) -> Random({rand})")
        cur = cur.next
    print()


# -----------------------------
# Main function to run program
# -----------------------------
if __name__ == "__main__":

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.next = n2
    n2.next = n3

    n1.random = n3
    n2.random = n1
    n3.random = None

    print("Original List:")
    print_list(n1)

    sol = Solution()
    copied = sol.copyRandomList(n1)

    print("Copied List:")
    print_list(copied)


# Time Complexity: O(n)
# Space Complexity: O(1)
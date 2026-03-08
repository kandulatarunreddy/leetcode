
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Example we follow through this code
        #
        # Input list:
        # 1 → 2 → 3 → 4 → 5
        # k = 3
        #
        # Goal:
        # Reverse first 3 nodes
        #
        # Expected result:
        # 3 → 2 → 1 → 4 → 5


        dummy = ListNode(0)
        dummy.next = head

        # dummy → 1 → 2 → 3 → 4 → 5
        #  ↑
        # prevGroup

        prevGroup = dummy

        while True:

            # -----------------------------
            # STEP 1: Find kth node
            # -----------------------------
            kth = prevGroup

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # After loop (k=3)
            #
            # dummy → 1 → 2 → 3 → 4 → 5
            #                   ↑
            #                  kth
            #
            # prevGroup = dummy


            nextGroup = kth.next

            # nextGroup = 4
            #
            # dummy → 1 → 2 → 3 → 4 → 5
            #                   ↑
            #                nextGroup


            # -----------------------------
            # STEP 2: Reverse the group
            # -----------------------------

            prev = nextGroup
            curr = prevGroup.next

            # prev = 4
            # curr = 1
            #
            # dummy → 1 → 2 → 3 → 4 → 5
            #          ↑
            #         curr


            while curr != nextGroup:

                temp = curr.next

                # Iteration 1
                # temp = 2


                curr.next = prev

                # 1 → 4 → 5
                #
                # reversed part starting:
                # 1 → 4


                prev = curr

                # prev = 1


                curr = temp

                # curr = 2


                # State now:
                #
                # reversed: 1 → 4
                # remaining: 2 → 3 → 4


                # Iteration 2
                #
                # temp = 3
                # 2.next = 1
                #
                # 2 → 1 → 4 → 5
                #
                # prev = 2
                # curr = 3


                # Iteration 3
                #
                # temp = 4
                # 3.next = 2
                #
                # 3 → 2 → 1 → 4 → 5
                #
                # prev = 3
                # curr = 4


            # Loop stops because curr == nextGroup (4)
            #
            # reversed group:
            #
            # 3 → 2 → 1 → 4 → 5


            # -----------------------------
            # STEP 3: Connect reversed group
            # -----------------------------

            temp = prevGroup.next

            # temp = 1
            #
            # 1 becomes tail of reversed group


            prevGroup.next = kth

            # dummy → 3 → 2 → 1 → 4 → 5


            prevGroup = temp

            # prevGroup now moves to 1
            #
            # dummy → 3 → 2 → 1 → 4 → 5
            #                   ↑
            #               prevGroup


            # Next iteration tries to find another group of k nodes
            #
            # Remaining nodes: 4 → 5
            # Count < k (3)
            #
            # Loop stops and we return result
# Helper function to create linked list
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy

    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next


# Helper function to print linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" → ")
        curr = curr.next
    print("None")


# ----------------------
# MAIN FUNCTION
# ----------------------
if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5]
    k = 3

    head = create_linked_list(arr)

    print("Original List:")
    print_list(head)

    sol = Solution()
    result = sol.reverseKGroup(head, k)

    print("\nReversed in K Group:")
    print_list(result)
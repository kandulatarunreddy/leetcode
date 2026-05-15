import heapq


# --------------------------------------------
# Definition for singly-linked list.
# --------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):

        """
        Problem:
        Merge k sorted linked lists
        into one sorted linked list.

        Example:

        list1: 1 -> 4 -> 5
        list2: 1 -> 3 -> 4
        list3: 2 -> 6

        Result:
        1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

        ----------------------------------------
        Key Idea:
        ----------------------------------------

        We only care about the SMALLEST
        current node among all lists.

        Current heads:

        1 -> 4 -> 5
        1 -> 3 -> 4
        2 -> 6

        Heap stores:
        [1, 1, 2]

        pick smallest = 1

        Then move that list forward.

        Repeat until heap becomes empty.

        Min Heap helps us get
        smallest node efficiently.
        """

        # Min heap
        heap = []

        # ----------------------------------------
        # Put first node of every list into heap
        #
        # Example:
        #
        # (1,0,node)
        # (1,1,node)
        # (2,2,node)
        #
        # Format:
        # (value, index, node)
        #
        # index avoids comparison error
        # when values are same.
        # ----------------------------------------
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # Dummy node for result list
        dummy = ListNode(0)

        # Pointer to build merged list
        current = dummy

        # ----------------------------------------
        # Process heap
        # ----------------------------------------
        while heap:

            # Get smallest node
            value, i, node = heapq.heappop(heap)

            # Add node to result
            current.next = node
            current = current.next

            # ------------------------------------
            # Move to next node in same list
            #
            # Example:
            #
            # popped:
            # 1 -> 4 -> 5
            #
            # push:
            # 4
            # ------------------------------------
            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next


"""
--------------------------------------------------
TIME COMPLEXITY (TC)
--------------------------------------------------

Let:

k = number of lists
N = total nodes across all lists

1. Heap initially stores k nodes:
   O(k log k)

2. Every node is pushed once:
   O(N log k)

3. Every node is popped once:
   O(N log k)

FINAL TIME COMPLEXITY:

O(N log k)

Why log(k)?

Because heap size is at most k
(one node from each list).


--------------------------------------------------
SPACE COMPLEXITY (SC)
--------------------------------------------------

Heap stores at most k nodes.

Space Complexity:

O(k)

Result linked list is excluded
from extra space analysis.
"""
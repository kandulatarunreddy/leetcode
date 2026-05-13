import heapq
from collections import defaultdict


class DualHeap:
    """
    We use TWO heaps:

    1. small = max heap
       stores SMALLER HALF of numbers

    2. large = min heap
       stores BIGGER HALF of numbers

    Why?

    Because median always lives in middle.

    Example:

    Window = [1,3,-1]

    Sorted:
    [-1,1,3]

    Split:

    small = [-1,1]
    large = [3]

    Median = 1
    """

    def __init__(self, k):

        # -----------------------------------
        # Max heap for smaller half
        #
        # Python only supports MIN heap.
        #
        # So we store NEGATIVE values
        # to simulate max heap.
        #
        # Example:
        # actual numbers [5,3]
        #
        # stored as:
        # [-5,-3]
        # -----------------------------------
        self.small = []

        # -----------------------------------
        # Min heap for larger half
        # -----------------------------------
        self.large = []

        # -----------------------------------
        # Lazy deletion dictionary
        #
        # Stores expired elements.
        #
        # Example:
        #
        # delayed[3] = 1
        #
        # means:
        # remove 3 later when
        # it reaches heap top.
        # -----------------------------------
        self.delayed = defaultdict(int)

        self.k = k

        # Valid element counts
        #
        # Needed because heaps may contain
        # expired elements temporarily.
        self.small_size = 0
        self.large_size = 0

    # ==========================================
    # REMOVE EXPIRED ELEMENTS
    # ==========================================
    def prune(self, heap):
        """
        Remove expired elements
        from heap TOP only.

        Why top only?

        Because removing random elements
        from heap is expensive.

        We wait until expired element
        naturally reaches top.
        """

        while heap:

            # -----------------------------------
            # Get actual number
            #
            # small heap stores negatives
            # -----------------------------------
            if heap == self.small:
                num = -heap[0]
            else:
                num = heap[0]

            # If expired
            if self.delayed[num] > 0:

                # Decrease delayed count
                self.delayed[num] -= 1

                # Remove from heap
                # Remove one element from the heap — specifically the top/root element.
                heapq.heappop(heap)

            else:
                break

    # ==========================================
    # BALANCE BOTH HEAPS
    # ==========================================
    def balance(self):
        """
        Rule:

        small can have:
        same size as large
        OR exactly 1 extra element

        Examples:

        Valid:
        small = 2, large = 2
        small = 3, large = 2

        Invalid:
        small = 4, large = 1
        """

        # -----------------------------------
        # small too big
        # -----------------------------------
        if self.small_size > self.large_size + 1:

            # Move top from small → large
            num = -heapq.heappop(self.small)

            heapq.heappush(self.large, num)

            self.small_size -= 1
            self.large_size += 1

            # Clean expired top
            self.prune(self.small)

        # -----------------------------------
        # large too big
        # -----------------------------------
        elif self.small_size < self.large_size:

            # Move top from large → small
            num = heapq.heappop(self.large)

            heapq.heappush(self.small, -num)

            self.large_size -= 1
            self.small_size += 1

            # Clean expired top
            self.prune(self.large)

    # ==========================================
    # ADD NEW NUMBER
    # ==========================================
    def add(self, num):
        """
        Add new number
        to correct heap.
        """

        # -----------------------------------
        # Goes to smaller half
        #
        # Compare against top of small
        # -----------------------------------
        if not self.small or num <= -self.small[0]:

            heapq.heappush(self.small, -num)

            self.small_size += 1

        # -----------------------------------
        # Goes to larger half
        # -----------------------------------
        else:
            heapq.heappush(self.large, num)

            self.large_size += 1

        # Rebalance heaps
        self.balance()

    # ==========================================
    # REMOVE OUTGOING ELEMENT
    # ==========================================
    def remove(self, num):
        """
        Remove expired number.

        We DON'T remove immediately.

        We mark for lazy deletion.
        """

        # Mark expired
        self.delayed[num] += 1

        # -----------------------------------
        # Determine which heap
        # -----------------------------------
        if num <= -self.small[0]:

            self.small_size -= 1

            # If top expired → clean now
            if num == -self.small[0]:
                self.prune(self.small)

        else:

            self.large_size -= 1

            # If top expired → clean now
            if self.large and num == self.large[0]:
                self.prune(self.large)

        # Balance again
        self.balance()

    # ==========================================
    # GET MEDIAN
    # ==========================================
    def median(self):
        """
        Return median.
        """

        # -----------------------------------
        # ODD window size
        #
        # Example:
        # [1,2,3]
        #
        # median = 2
        # -----------------------------------
        if self.k % 2 == 1:
            return float(-self.small[0])

        # -----------------------------------
        # EVEN window size
        #
        # Example:
        # [1,2,3,4]
        # small=[-2,-1]
        # large=[3,4]
        # median = (2+3)/2
        # -----------------------------------
        return (-self.small[0] + self.large[0]) / 2


# ==========================================
# MAIN FUNCTION
# ==========================================
def sliding_window_median(nums, k):

    # Create heap manager
    dh = DualHeap(k)

    result = []

    # Traverse array
    for i in range(len(nums)):

        # -----------------------------------
        # Add current number
        # -----------------------------------
        dh.add(nums[i])

        # -----------------------------------
        # First window forms when:
        #
        # i >= k - 1
        # -----------------------------------
        if i >= k - 1:

            # Get median
            result.append(dh.median())

            # -----------------------------------
            # Remove outgoing element
            #
            # Example:
            #
            # i = 4
            # k = 3
            #
            # outgoing index:
            # i-k+1 = 2
            # -----------------------------------
            outgoing = nums[i - k + 1]

            dh.remove(outgoing)

    return result


# ==========================================
# RUN PROGRAM
# ==========================================
if __name__ == "__main__":

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    answer = sliding_window_median(nums, k)

    print("Input Array:", nums)
    print("Window Size:", k)
    print("Sliding Window Median:", answer)
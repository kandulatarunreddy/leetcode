import heapq


class MedianFinder:

    def __init__(self):

        # ---------------------------------
        # Max heap (smaller half)
        #
        # Python only supports min heap.
        #
        # So we store NEGATIVE values.
        #
        # Example:
        # [5,3]
        #
        # stored as:
        # [-5,-3]
        # ---------------------------------
        self.small = []

        # ---------------------------------
        # Min heap (larger half)
        # ---------------------------------
        self.large = []

    # =====================================
    # ADD NUMBER
    # =====================================
    def addNum(self, num):

        # ---------------------------------
        # Add to small heap first
        # ---------------------------------
        heapq.heappush(self.small, -num)

        # ---------------------------------
        # Ensure correct ordering:
        #
        # largest value in small
        # must be <= smallest value in large
        #
        # If violated,
        # move element to correct heap
        # ---------------------------------
        if self.large and -self.small[0] > self.large[0]:

            value = -heapq.heappop(self.small)

            heapq.heappush(self.large, value)

        # ---------------------------------
        # Balance heaps
        #
        # small can have:
        # same size
        # OR one extra
        # ---------------------------------

        # small too big
        if len(self.small) > len(self.large) + 1:

            value = -heapq.heappop(self.small)

            heapq.heappush(self.large, value)

        # large too big
        '''Because else means:
                "small is NOT too big"
           But that does not automatically mean:
            "large is too big"
        Balanced state:
            small = 2
            large = 2
        First condition:
            2 > 3 → False
        else would run incorrectly and move an element even though heaps are already balanced.
            '''
        if len(self.large) > len(self.small):

            value = heapq.heappop(self.large)

            heapq.heappush(self.small, -value)

    # =====================================
    # FIND MEDIAN
    # =====================================
    def findMedian(self):

        # ---------------------------------
        # Odd total count
        #
        # Example:
        # [1,2,3]
        #
        # median = 2
        # ---------------------------------
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # ---------------------------------
        # Even total count
        #
        # Example:
        # [1,2,3,4]
        #
        # median = (2+3)/2
        # ---------------------------------
        return (-self.small[0] + self.large[0]) / 2


# =====================================
# MAIN
# =====================================
if __name__ == "__main__":

    mf = MedianFinder()

    mf.addNum(1)
    mf.addNum(2)

    print(mf.findMedian())   # 1.5

    mf.addNum(3)

    print(mf.findMedian())   # 2.0
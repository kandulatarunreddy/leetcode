import heapq

class KthLargest:

    def __init__(self, k, nums):
        """
        Initialize the object with k and initial stream
        """
        self.k = k
        self.min_heap = []

        # Build heap with initial numbers
        for num in nums:
            heapq.heappush(self.min_heap, num)

            # Maintain size k
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

    def add(self, val):
        """
        Add new value and return kth largest
        """
        heapq.heappush(self.min_heap, val)

        # Keep only k elements
        #adding new element modify heap so rearrange heap
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # Root is kth largest
        return self.min_heap[0]


# -----------------------------
# Driver Code
# -----------------------------
if __name__ == "__main__":
    k = 3
    nums = [4, 5, 8, 2]

    kthLargest = KthLargest(k, nums)

    print(kthLargest.add(3))   # returns 4
    print(kthLargest.add(5))   # returns 5
    print(kthLargest.add(10))  # returns 5
    print(kthLargest.add(9))   # returns 8
    print(kthLargest.add(4))   # returns 8


# Time Complexity:
# add(): O(log k)
# constructor: O(N log k)

# Space Complexity:
# O(k)
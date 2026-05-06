import heapq

def findKthLargest(nums, k):
    # Step 1: Create empty min heap
    min_heap = []

    # Step 2: Process each number
    for num in nums:
        heapq.heappush(min_heap, num)

        # Keep heap size = k
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 3: Top of heap = kth largest
    return min_heap[0]


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2

    print("Kth Largest:", findKthLargest(nums, k))


# Time Complexity: O(N log k)
# Space Complexity: O(k)
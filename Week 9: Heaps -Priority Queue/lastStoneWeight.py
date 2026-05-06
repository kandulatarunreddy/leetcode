import heapq

def lastStoneWeight(stones):
    # -----------------------------
    # Step 1: Convert to max heap
    # (store negative values)
    # -----------------------------
    max_heap = [-s for s in stones]
    heapq.heapify(max_heap)

    # -----------------------------
    # Step 2: Process until ≤1 stone
    # -----------------------------
    while len(max_heap) > 1:
        # Take two largest stones
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)

        # If not equal, push difference
        if first != second:
            heapq.heappush(max_heap, -(first - second))

    # -----------------------------
    # Step 3: Return result
    # -----------------------------
    return -max_heap[0] if max_heap else 0


# -----------------------------
# Driver Code
# -----------------------------
if __name__ == "__main__":
    stones = [2,7,4,1,8,1]

    print("Last Stone Weight:", lastStoneWeight(stones))


# Time Complexity: O(N log N)
# Space Complexity: O(N)
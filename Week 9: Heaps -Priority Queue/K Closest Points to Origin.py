import heapq

def kClosest(points, k):
    max_heap = []

    for x, y in points:
        dist = x*x + y*y

        # push negative distance for max heap
        heapq.heappush(max_heap, (-dist, x, y))

        # keep only k points
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    # extract result
    return [[x, y] for (_, x, y) in max_heap]


if __name__ == "__main__":
    points = [[1,3],[-2,2],[5,8],[0,1]]
    k = 2

    print("K Closest:", kClosest(points, k))


# Time Complexity: O(N log k)
# Space Complexity: O(k)
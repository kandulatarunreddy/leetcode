import heapq

def findCheapestPrice(n, flights, src, dst, k):
    """
    Problem: Cheapest Flights Within K Stops

    We are given:
    - n: number of nodes (cities)
    - flights: list of edges (u, v, price)
    - src: source node
    - dst: destination node
    - k: maximum number of stops allowed

    Goal:
    Find the cheapest cost from src to dst with at most k stops.
    If not possible, return -1.

    ------------------------------------------------------------
    APPROACH: Modified Dijkstra (Min Heap / Priority Queue)
    ------------------------------------------------------------

    Key Idea:
    Standard Dijkstra only tracks the minimum distance to each node.
    However, here we must also track the number of stops.

    So each state in the heap will be:
        (current_cost, current_node, stops_used)

    Why?
    Because reaching the same node with fewer stops may be better,
    even if the cost is slightly higher.

    ------------------------------------------------------------
    STEPS:
    ------------------------------------------------------------
    1. Build adjacency list (graph)
    2. Use a min-heap (priority queue) storing:
         (cost, node, stops)
    3. Pop the cheapest state
    4. If destination is reached → return cost
    5. If stops exceed k → skip
    6. Explore neighbors and push new states into heap
    7. Use a visited dictionary to prune worse states
    """

    # Step 1: Build graph (adjacency list)
    graph = {i: [] for i in range(n)}
    for u, v, price in flights:
        graph[u].append((v, price))

    # Step 2: Min heap initialization
    # (cost, current_node, stops_used)
    pq = [(0, src, 0)]

    # Step 3: Visited dictionary
    # Key: (node, stops)
    # Value: minimum cost found so far for this state
    visited = {}

    # Step 4: Process heap
    while pq:
        cost, node, stops = heapq.heappop(pq)

        # Step 5: If destination reached, return cost
        # This works because heap always pops the minimum cost first
        if node == dst:
            return cost

        # Step 6: If stops exceed allowed limit, skip
        if stops > k:
            continue

        # Step 7: Pruning
        # If we've already seen this (node, stops) with a cheaper cost, skip
        if (node, stops) in visited and visited[(node, stops)] <= cost:
            continue

        # Record this state
        visited[(node, stops)] = cost

        # Step 8: Explore neighbors
        for neighbor, price in graph[node]:
            new_cost = cost + price
            heapq.heappush(pq, (new_cost, neighbor, stops + 1))

    # Step 9: If destination not reachable within k stops
    return -1


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    n = 4
    flights = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 3, 5)
    ]
    src = 0
    dst = 3
    k = 1

    print(findCheapestPrice(n, flights, src, dst, k))


"""
------------------------------------------------------------
TIME COMPLEXITY (TC)
------------------------------------------------------------

Let:
    V = number of nodes
    E = number of edges
    K = maximum stops allowed

Each node can be processed up to (K + 1) times (for different stops).

Heap operations take O(log (V * K)).

So overall complexity:

    O((E * K) * log(V * K))

In worst case (dense graph):

    O(E * K * log(VK))


------------------------------------------------------------
SPACE COMPLEXITY (SC)
------------------------------------------------------------

1. Graph storage:
    O(V + E)

2. Heap (priority queue):
    In worst case, it may store O(V * K) states

3. Visited dictionary:
    O(V * K)

Total Space Complexity:

    O(V + E + V * K)


------------------------------------------------------------
KEY TAKEAWAYS
------------------------------------------------------------

- We cannot use standard Dijkstra because it ignores stop constraints.
- We must track both cost AND stops.
- Same node can be revisited with different stop counts.
- Priority queue ensures we always explore cheapest paths first.
"""
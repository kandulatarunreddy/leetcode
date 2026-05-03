import heapq

def dijkstra(graph, source):
    """
    graph: adjacency list
    graph[u] = [(v, weight), ...]
    """

    n = len(graph)

    # Distance array
    dist = [float('inf')] * n
    dist[source] = 0

    # Min heap (distance, node)
    pq = [(0, source)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        # Skip if we already found a better path
        if current_dist > dist[node]:
            continue

        # Relax neighbors
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


# -------------------------
# Example Graph
# -------------------------
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

print(dijkstra(graph, 0))
from collections import deque

def findOrder(numCourses, prerequisites):
    """
    Return a valid course order using Kahn's Algorithm (BFS)
    If cycle exists → return []
    """

    # Step 1: Build graph
    graph = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Step 2: Start with nodes having 0 in-degree
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    order = []

    # Step 3: Process queue
    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check if valid
    if len(order) == numCourses:
        return order
    else:
        return []  # cycle exists


# ---------------- Example 1 ----------------
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

print("Course Order:", findOrder(numCourses, prerequisites))
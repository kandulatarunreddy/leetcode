from collections import deque

def canFinish(numCourses, prerequisites):
    """
    Detect cycle using Kahn's Algorithm (Topological Sort BFS)
    """

    # Step 1: Build graph
    graph = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Step 2: Add courses with no prerequisites
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    completed = 0  # count of processed courses

    # Step 3: Process queue
    while queue:
        node = queue.popleft()
        completed += 1

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check if all courses processed
    return completed == numCourses


# -------- Example --------
numCourses = 4
prerequisites = [[1,0],[2,1],[3,2]]

print(canFinish(numCourses, prerequisites))  # True
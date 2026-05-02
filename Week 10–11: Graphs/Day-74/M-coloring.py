# Function to check if it's safe to assign a color to a node
def is_safe(node, graph, colors, color):
    """
    Returns True if no adjacent node has the same color.
    """
    for neighbor in range(len(graph)):

        # Check if neighbor is connected AND has same color
        if graph[node][neighbor] == 1 and colors[neighbor] == color:
            return False

    return True


def solve_m_coloring(graph, m, colors, node):

    # If all nodes are colored → success
    if node == len(graph):
        return True

    # Try all colors
    for color in range(1, m + 1):

        # -------------------------------
        # STEP 1: LOCAL CHECK
        # -------------------------------
        # is_safe = TRUE means:
        # "This color does NOT conflict with already colored neighbors"
        if is_safe(node, graph, colors, color):

            # Assign color (decision made)
            colors[node] = color

            # -------------------------------
            # STEP 2: GLOBAL CHECK (RECURSION)
            # -------------------------------
            # Even though current placement is safe,
            # deeper nodes may FAIL later → so we check recursively
            if solve_m_coloring(graph, m, colors, node + 1):

                # If recursion succeeds → entire path is valid
                return True

            # -------------------------------
            # BACKTRACK CASE (IMPORTANT)
            # -------------------------------
            # This happens when:
            # is_safe(node, color) == True  BUT
            # deeper recursion returns False

            # Meaning:
            # "This choice looked correct now,
            #  but it leads to failure later"
            colors[node] = 0  # undo decision

    # No color worked for this node
    return False


# Main function
def graph_coloring(graph, m):
    """
    Initializes color array and starts backtracking
    """
    n = len(graph)
    colors = [0] * n  # 0 means no color assigned

    if solve_m_coloring(graph, m, colors, 0):
        return colors
    else:
        return None


# -----------------------------
# Main function
# -----------------------------
def graph_coloring(graph, m):
    n = len(graph)

    # Initially no node is colored
    colors = [0] * n

    if solve_m_coloring(graph, m, colors, 0):
        return colors
    else:
        return None


# -----------------------------
# Example 1 (SUCCESS)
# -----------------------------
graph1 = [
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

m1 = 3

print("Example 1:")
res1 = graph_coloring(graph1, m1)
print(res1)


# -----------------------------
# Example 2 (FAIL)
# -----------------------------
graph2 = [
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

m2 = 2

print("\nExample 2:")
res2 = graph_coloring(graph2, m2)
print(res2)
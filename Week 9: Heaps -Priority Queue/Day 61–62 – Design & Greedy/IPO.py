import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        """
        IPO PROBLEM

        --------------------------------------------
        Problem:
        --------------------------------------------
        You are given:
        - k = max number of projects you can do
        - w = initial capital (money you start with)
        - capital[i] = money required to start project i
        - profits[i] = money earned after completing project i

        Goal:
        Maximize final capital after doing at most k projects.

        --------------------------------------------
        Key Idea:
        --------------------------------------------
        At each step:
        1. Pick all projects you can afford (capital <= w)
        2. From them, choose the one with maximum profit
        3. Add profit to w
        4. Repeat k times

        We use:
        - Sorting → to process affordable projects in order
        - Max Heap → to always pick max profit quickly
        """

        # --------------------------------------------
        # Step 1: Combine capital and profit
        #
        # Example:
        # profits =  [1, 2, 3]
        # capital =  [0, 1, 1]
        #
        # Combined:
        # [(0,1), (1,2), (1,3)]
        #
        # Meaning:
        # (capital_required, profit)
        # --------------------------------------------
        projects = list(zip(capital, profits))

        # Sort by capital required
        # So we can process affordable projects in order
        projects.sort()

        # --------------------------------------------
        # Max Heap (store profits)
        #
        # Python only has MIN heap,
        # so we store negative values to simulate MAX heap.
        #
        # Example heap:
        # [-3, -2] means profits [3, 2]
        # --------------------------------------------
        max_heap = []

        i = 0  # pointer to projects list
        n = len(projects)

        # --------------------------------------------
        # We can do at most k projects
        # --------------------------------------------
        for step in range(k):

            # ----------------------------------------
            # Add all projects we can currently afford
            #
            # Condition:
            # capital_required <= current_w
            #
            # Example:
            # w = 1
            # add projects with capital 0 or 1
            # ----------------------------------------
            while i < n and projects[i][0] <= w:
                cap = projects[i][0]
                profit = projects[i][1]

                heapq.heappush(max_heap, -profit)
                i += 1

            # ----------------------------------------
            # If no project is available, stop early
            # ----------------------------------------
            if not max_heap:
                break

            # ----------------------------------------
            # Pick project with maximum profit
            #
            # Example:
            # heap = [-3, -2]
            # pop -> -3 -> profit = 3
            # ----------------------------------------
            best_profit = -heapq.heappop(max_heap)

            # Add profit to current capital
            w += best_profit

        return w


# ----------------------------------------------------
# Example run (you can execute in IntelliJ)
# ----------------------------------------------------
if __name__ == "__main__":

    solution = Solution()

    # Example:
    # k = 2 projects allowed
    # w = 0 initial capital
    #
    # Projects:
    # capital = [0, 1, 1]
    # profits = [1, 2, 3]
    #
    # Step 1:
    # start w = 0 → only project (0,1) is available
    # take it → w = 1
    #
    # Step 2:
    # w = 1 → projects (1,2) and (1,3) available
    # pick max profit = 3 → w = 4
    #
    # Final answer = 4

    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]

    result = solution.findMaximizedCapital(k, w, profits, capital)

    print("Final Maximized Capital:", result)


"""
------------------------------------------------------------
TIME COMPLEXITY (TC)
------------------------------------------------------------

Let:
n = number of projects
k = number of selections

1. Sorting projects:
   O(n log n)

2. Each project is pushed into heap at most once:
   O(n log n)

3. Each selection pops from heap:
   O(k log n)

FINAL TIME COMPLEXITY:
O(n log n + k log n)

Since k ≤ n in most cases:
≈ O(n log n)


------------------------------------------------------------
SPACE COMPLEXITY (SC)
------------------------------------------------------------

1. Projects list: O(n)
2. Max heap (worst case all projects): O(n)

FINAL SPACE COMPLEXITY:
O(n)
"""
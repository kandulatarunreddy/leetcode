from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    # prev2 -> min cost to reach step i-2
    # prev1 -> min cost to reach step i-1
    prev2 = 0
    prev1 = 0

    # iterate through each step
    for c in cost:
        # choose cheaper of previous two steps
        curr = c + min(prev1, prev2)

        # shift for next iteration
        prev2 = prev1
        prev1 = curr

    # can finish from last or second last step
    return min(prev1, prev2)
'''class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
        
'''


if __name__ == "__main__":
    # Example test cases
    cost1 = [10, 15, 20]
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    print("Input:", cost1)
    print("Min Cost:", minCostClimbingStairs(cost1))
    print()

    print("Input:", cost2)
    print("Min Cost:", minCostClimbingStairs(cost2))
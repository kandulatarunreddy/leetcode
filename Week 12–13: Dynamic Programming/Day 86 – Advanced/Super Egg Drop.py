class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        dp[i] = maximum number of floors that can be GUARANTEED
                to be solved using current number of moves and i eggs.

        IMPORTANT:
        - This is NOT number of floors tested so far
        - This is NOT simulation of dropping eggs

        It represents CAPABILITY:
        → how many floors we can ALWAYS solve in worst case
        """

        # dp[i] = floors we can handle with i eggs and current moves
        # Initially: 0 moves → we can handle 0 floors
        dp = [0] * (k + 1)

        moves = 0

        # Keep increasing moves until we can cover all n floors
        while dp[k] < n:
            moves += 1

            # IMPORTANT:
            # We iterate backwards so we use values from previous move only
            for i in range(k, 0, -1):

                # dp[i-1] → if egg BREAKS → we can explore BELOW floors
                # dp[i]   → if egg SURVIVES → we can explore ABOVE floors
                # +1      → current floor where we drop the egg

                dp[i] = dp[i] + dp[i - 1] + 1

        return moves


# -------------------- TEST --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.superEggDrop(2, 6))  # Output: 3

# -------------------- INTUITION NOTES --------------------

"""
🔑 KEY IDEA:
We are NOT finding the exact breaking floor directly.

We are building a strategy that GUARANTEES we can find it.

------------------------------------------------------------

📌 IMPORTANT CORE INSIGHT:

With only 1 move, you can only make 1 decision (1 drop),
no matter how many eggs you have.

So:

Move = 1:
    1 egg → 1 floor
    2 eggs → 1 floor
    3 eggs → 1 floor
    (because only ONE drop is possible)

------------------------------------------------------------

Move = 2:
    1 egg → 2 floors
    2 eggs → 3 floors

Move = 3:
    1 egg → 3 floors
    2 eggs → 6 floors   ← grows fast

------------------------------------------------------------

🧠 WHY THIS WORKS:

Each move creates a split:

    if egg breaks   → search below (dp[i-1])
    if egg survives → search above (dp[i])

So each move expands coverage:

    below + current + above

------------------------------------------------------------

🚀 FINAL INTUITION:

dp[i] is NOT history of tests.

dp[i] is the total number of floors we can ALWAYS resolve
using i eggs and given number of moves.

------------------------------------------------------------
"""


# Time Complexity: O(k * moves), where moves ≈ O(log n)
# Space Complexity: O(k)
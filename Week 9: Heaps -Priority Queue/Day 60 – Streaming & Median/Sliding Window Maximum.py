from collections import deque


def max_sliding_window(nums, k):
    dq = deque()      # stores indices
    result = []

    print("\n================ START ==================\n")

    for i in range(len(nums)):

        print(f"\n👉 i = {i}, nums[i] = {nums[i]}")

        # -----------------------------
        # STEP 1: Remove expired indices
        # -----------------------------
        # Window is: [i-k+1 ... i]
        #
        # Any index <= i-k is OUTSIDE window
        #
        if dq:
            print(f"   Before cleanup dq = {list(dq)}")
            print(f"   Window should be [{i-k+1} to {i}]")

        if dq and dq[0] <= i - k:
            print(f"   ❌ Removing expired index {dq[0]} (nums[{dq[0]}]={nums[dq[0]]})")
            dq.popleft()

        # -----------------------------
        # STEP 2: Remove smaller elements
        # -----------------------------
        while dq and nums[dq[-1]] < nums[i]:
            print(f"   ❌ Removing smaller nums[{dq[-1]}]={nums[dq[-1]]}")
            dq.pop()

        # -----------------------------
        # STEP 3: Add current index
        # -----------------------------
        dq.append(i)

        print(f"   ✅ After insert dq = {list(dq)}")
        print(f"   (values = {[nums[x] for x in dq]})")

        # -----------------------------
        # STEP 4: Record answer
        #start recording result only when i reaches k-1
        # -----------------------------
        if i >= k - 1:
            print(f"   👉 Window [{i-k+1}, {i}] = {[nums[j] for j in range(i-k+1, i+1)]}")
            print(f"   👉 dq[0] = {dq[0]} → max = {nums[dq[0]]}")
            result.append(nums[dq[0]])

    print("\n================ END ==================\n")

    return result


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    ans = max_sliding_window(nums, k)

    print("FINAL ANSWER:", ans)
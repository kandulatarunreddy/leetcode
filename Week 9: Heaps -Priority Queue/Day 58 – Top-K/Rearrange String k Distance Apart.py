from collections import Counter, deque
import heapq


def rearrangeString(s: str, k: int) -> str:
    """
    Rearrange the string so that the same characters
    are at least k distance apart.

    Return "" if impossible.
    """

    # If k <= 1, no restriction needed
    if k <= 1:
        return s

    # Count frequency of each character
    freq = Counter(s)

    # ---------------------------------------------------
    # Python has a MIN heap
    # Use negative counts to simulate MAX heap
    #
    # Example:
    # [('a', 3), ('b', 2)]
    #
    # becomes:
    # [(-3, 'a'), (-2, 'b')]
    # ---------------------------------------------------
    max_heap = [(-count, char) for char, count in freq.items()]

    # Convert normal list into heap
    heapq.heapify(max_heap)

    # ---------------------------------------------------
    # Queue stores characters during cooldown
    #
    # Format:
    # (remaining_count, char, next_valid_index)
    #
    # Example:
    # (-2, 'a', 5)
    #
    # Means:
    # - 'a' still needs 2 more placements
    # - cannot be reused until index 5
    # ---------------------------------------------------
    wait_queue = deque()

    result = []

    # Current position in result string
    index = 0

    # Continue while:
    # - heap still has available chars OR
    # - queue still has cooling chars
    while max_heap or wait_queue:

        # ---------------------------------------------------
        # Step 1:
        # Release characters whose cooldown expired
        # ---------------------------------------------------
        if wait_queue and wait_queue[0][2] <= index:

            count, char, _ = wait_queue.popleft()

            # Push back into heap so it can be reused
            heapq.heappush(max_heap, (count, char))

        # ---------------------------------------------------
        # If heap empty but queue still has chars cooling,
        # then arrangement is impossible
        # ---------------------------------------------------
        if not max_heap:
            return ""

        # ---------------------------------------------------
        # Step 2:
        # Pick character with highest remaining frequency
        # ---------------------------------------------------
        count, char = heapq.heappop(max_heap)

        # Add char to answer
        result.append(char)

        # ---------------------------------------------------
        # Since count is negative:
        #
        # Example:
        # -3 -> -2
        #
        # meaning one occurrence used
        # ---------------------------------------------------
        count += 1

        # ---------------------------------------------------
        # If still more copies left,
        # put into cooldown queue
        # ---------------------------------------------------
        if count < 0:
            next_valid_index = index + k

            wait_queue.append(
                (count, char, next_valid_index)
            )

        # Move to next position
        index += 1

    return ''.join(result)


# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------

s = "aabbcc"
k = 3

print(rearrangeString(s, k))
#Tc: O(n log m)
#sc:O(m)n = length of string , m = unique chars
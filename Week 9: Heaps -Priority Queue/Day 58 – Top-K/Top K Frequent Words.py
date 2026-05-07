from collections import Counter
import heapq

def topKFrequent(words, k):
    # Step 1: Count frequency of each word
    # Example: ["i","love","leetcode","i","love","coding"]
    # count = {"i":2, "love":2, "leetcode":1, "coding":1}
    count = Counter(words)

    # Step 2: Build a heap of (-frequency, word)
    # Negative frequency because Python has a min-heap,
    # and we want highest frequency first
    heap = []
    for word, freq in count.items():
        heap.append((-freq, word))

    # Convert list into a heap in O(n)
    heapq.heapify(heap)
    print(heap)

    # Step 3: Extract top k elements
    result = []
    for _ in range(k):
        freq, word = heapq.heappop(heap)
        result.append(word)

    return result


# Example usage
if __name__ == "__main__":
    words = ["i","love","leetcode","i","love","coding"]
    k = 2
    print(topKFrequent(words, k))  # Output: ["i", "love"]

# Time Complexity: O(n log k)  (heap operations k times after O(n) build)
# Space Complexity: O(n)       (for hashmap + heap)
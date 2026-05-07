from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)
    # Step 1: create buckets
    buckets = [[] for _ in range(len(nums) + 1)]
    # Step 2: fill buckets
    for num, count in freq.items():
        buckets[count].append(num)
    # Step 3: collect top k
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    print("Top K Frequent:", topKFrequent(nums, k))


# Time Complexity: O(N)
# Space Complexity: O(N)
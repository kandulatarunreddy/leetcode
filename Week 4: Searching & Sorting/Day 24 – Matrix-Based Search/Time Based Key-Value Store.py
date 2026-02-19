from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Store dictionary with key -> list of (value, timestamp)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append (value, timestamp) to the list for this key
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Get list of values for key, default empty list
        values = self.store.get(key, [])
        res = ''
        l, r = 0, len(values) - 1

        # Binary search for largest timestamp <= given timestamp
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]  # possible answer
                l = mid + 1
            else:
                r = mid - 1
        return res

if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))  # Output: "bar"
    print(tm.get("foo", 3))  # Output: "bar"
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))  # Output: "bar2"
    print(tm.get("foo", 5))  # Output: "bar2"

# Time Complexity: O(log n) for get, O(1) for set
# Space Complexity: O(n) for storing all key-value-timestamp entries
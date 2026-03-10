# Node for Doubly Linked List
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # Maximum capacity of cache
        self.cap = capacity

        # HashMap to store key -> node
        self.cache = {}

        # Dummy nodes for LRU (left) and MRU (right)
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Connect dummy nodes
        self.left.next = self.right
        self.right.prev = self.left


    # Remove a node from the doubly linked list
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev


    # Insert node at MRU position (before right dummy)
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node


    # Get value for key
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # Move node to MRU position
            self.remove(node)
            self.insert(node)

            return node.val

        return -1


    # Insert or update key-value pair
    def put(self, key: int, value: int) -> None:

        # If key exists remove old node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)

        # Add to hashmap
        self.cache[key] = node

        # Insert at MRU side
        self.insert(node)

        # If capacity exceeded remove LRU node
        if len(self.cache) > self.cap:

            # LRU node is right after left dummy
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]


# -----------------------------
# Main method (Test the cache)
# -----------------------------
if __name__ == "__main__":

    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)

    print(cache.get(1))  # Expected: 1

    cache.put(3, 3)      # Evicts key 2

    print(cache.get(2))  # Expected: -1

    cache.put(4, 4)      # Evicts key 1

    print(cache.get(1))  # Expected: -1
    print(cache.get(3))  # Expected: 3
    print(cache.get(4))  # Expected: 4

#SC:O(capacity)
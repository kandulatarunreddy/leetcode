class Node:
    """
    Doubly Linked List Node

    Each node stores:
    - key
    - value
    - prev pointer
    - next pointer
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        # Maximum number of items cache can hold
        self.capacity = capacity

        # HashMap:
        # key -> node reference
        #
        # Example:
        # {
        #   1: node1,
        #   2: node2
        # }
        #
        # Why?
        # So lookup becomes O(1)
        self.cache = {}

        # Dummy nodes
        #
        # We use dummy nodes to avoid
        # edge-case handling.
        #
        # Structure:
        #
        # left(dummy) <-> right(dummy)
        #
        # left side = LRU
        # right side = MRU

        self.left = Node(0, 0)    # LRU dummy
        self.right = Node(0, 0)   # MRU dummy

        # Connect dummy nodes
        self.left.next = self.right
        self.right.prev = self.left

    # -------------------------------------------------
    # Remove node from linked list
    # -------------------------------------------------
    def remove(self, node):

        """
        Example:

        Before removing 2:

        left <-> 1 <-> 2 <-> 3 <-> right

        remove(2)

        After:

        left <-> 1 <-> 3 <-> right
        """

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # -------------------------------------------------
    # Insert node at MRU position (right side)
    # -------------------------------------------------
    def insert(self, node):

        """
        We always insert near RIGHT.

        Why?

        RIGHT = Most Recently Used (MRU)

        Example:

        Before:

        left <-> 1 <-> 2 <-> right

        insert(3)

        After:

        left <-> 1 <-> 2 <-> 3 <-> right
                                  ↑
                                 MRU
        """

        # Node before right dummy
        prev_right = self.right.prev

        # Connect previous node -> new node
        prev_right.next = node
        node.prev = prev_right

        # Connect new node -> right dummy
        node.next = self.right
        self.right.prev = node

    # -------------------------------------------------
    # GET
    # -------------------------------------------------
    def get(self, key: int) -> int:

        """
        Return value if key exists.
        Otherwise return -1.

        IMPORTANT:
        If key is accessed,
        it becomes MOST RECENTLY USED.

        Example:

        Cache:

        left <-> 1 <-> 2 <-> 3 <-> right
                  LRU            MRU

        get(2)

        Since 2 was used,
        move it to MRU side.

        Result:

        left <-> 1 <-> 3 <-> 2 <-> right
        """

        # Key not found
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Remove from current position
        self.remove(node)

        # Move to MRU side
        self.insert(node)

        return node.value

    # -------------------------------------------------
    # PUT
    # -------------------------------------------------
    def put(self, key: int, value: int) -> None:

        """
        Add new key-value pair.

        OR

        Update existing key.

        Example:

        capacity = 2

        put(1,1)

        Cache:
        left <-> 1 <-> right

        ----------------------

        put(2,2)

        Cache:
        left <-> 1 <-> 2 <-> right

        ----------------------

        put(3,3)

        Capacity exceeded.

        Remove LRU (1)

        Final:
        left <-> 2 <-> 3 <-> right
        """

        # If key already exists:
        # remove old node first
        #
        # Example:
        #
        # put(2, 100)
        #
        # old node(2) removed
        # new node(2,100) inserted
        if key in self.cache:
            old_node = self.cache[key]

            self.remove(old_node)

            # Remove old reference
            del self.cache[key]

        # Create new node
        new_node = Node(key, value)

        # Add to hashmap
        self.cache[key] = new_node

        # Insert into linked list
        # at MRU side
        self.insert(new_node)

        # If capacity exceeded:
        if len(self.cache) > self.capacity:

            """
            LRU node is always:

            left.next

            Example:

            left <-> 1 <-> 2 <-> 3 <-> right
                     ↑

                  left.next

            So remove 1.
            """

            lru = self.left.next

            # Remove from linked list
            self.remove(lru)

            # Remove from hashmap
            del self.cache[lru.key]


# =====================================================
# EXAMPLE WALKTHROUGH
# =====================================================

cache = LRUCache(2)

# -----------------------------------------------------
# put(1,1)
# -----------------------------------------------------
cache.put(1, 1)

# Cache:
#
# left <-> 1 <-> right
#
# 1 = MRU and LRU


# -----------------------------------------------------
# put(2,2)
# -----------------------------------------------------
cache.put(2, 2)

# Cache:
#
# left <-> 1 <-> 2 <-> right
#
# 1 = LRU
# 2 = MRU


# -----------------------------------------------------
# get(1)
# -----------------------------------------------------
print(cache.get(1))  # Output: 1

# Since 1 was accessed,
# move it to MRU side
#
# Cache becomes:
#
# left <-> 2 <-> 1 <-> right
#
# 2 = LRU
# 1 = MRU


# -----------------------------------------------------
# put(3,3)
# -----------------------------------------------------
cache.put(3, 3)

# Capacity exceeded
#
# Remove LRU = 2
#
# Cache:
#
# left <-> 1 <-> 3 <-> right


# -----------------------------------------------------
# get(2)
# -----------------------------------------------------
print(cache.get(2))  # Output: -1

# Because 2 was removed


# -----------------------------------------------------
# put(4,4)
# -----------------------------------------------------
cache.put(4, 4)

# Capacity exceeded
#
# Remove LRU = 1
#
# Cache:
#
# left <-> 3 <-> 4 <-> right


# -----------------------------------------------------
# Final checks
# -----------------------------------------------------
print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4
from collections import defaultdict


# -------------------------------------------------
# Node
# -------------------------------------------------
class Node:
    def __init__(self, key, value):

        self.key = key
        self.value = value

        # Frequency count
        self.freq = 1

        self.prev = None
        self.next = None


# -------------------------------------------------
# Doubly Linked List
# Used for each frequency
# -------------------------------------------------
class DoublyLinkedList:

    def __init__(self):

        # Dummy nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0

    def insert(self, node):
        """
        Insert node at MRU side (right)

        Example:

        left <-> 1 <-> 2 <-> right

        insert(3)

        left <-> 1 <-> 2 <-> 3 <-> right
        """

        prev_right = self.right.prev

        prev_right.next = node
        node.prev = prev_right

        node.next = self.right
        self.right.prev = node

        self.size += 1

    def remove(self, node):
        """
        Remove node

        Example:

        left <-> 1 <-> 2 <-> 3 <-> right

        remove(2)

        left <-> 1 <-> 3 <-> right
        """

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1

    def remove_lru(self):
        """
        Remove least recently used node.

        Example:

        left <-> 1 <-> 2 <-> 3 <-> right

        remove 1
        """

        if self.size == 0:
            return None

        lru = self.left.next
        self.remove(lru)

        return lru


# -------------------------------------------------
# LFU Cache
# -------------------------------------------------
class LFUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.size = 0

        # key -> node
        self.key_to_node = {}

        # freq -> doubly linked list
        self.freq_to_list = defaultdict(DoublyLinkedList)

        # minimum frequency
        self.min_freq = 0

    def update_frequency(self, node):

        """
        Move node from old frequency
        to new frequency.

        Example:

        node freq = 1

        remove from freq=1 list
        add to freq=2 list
        """

        old_freq = node.freq

        # Remove from old frequency list
        self.freq_to_list[old_freq].remove(node)

        # If old freq list became empty
        # update min frequency
        if (
                old_freq == self.min_freq
                and self.freq_to_list[old_freq].size == 0
        ):
            self.min_freq += 1

        # Increase frequency
        node.freq += 1

        # Insert into new frequency list
        self.freq_to_list[node.freq].insert(node)

    # -------------------------------------------------
    # GET
    # -------------------------------------------------
    def get(self, key: int) -> int:

        """
        Example:

        get(2)

        increase frequency
        """

        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]

        # update usage frequency
        self.update_frequency(node)

        return node.value

    # -------------------------------------------------
    # PUT
    # -------------------------------------------------
    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        # Key already exists
        if key in self.key_to_node:

            node = self.key_to_node[key]

            # Update value
            node.value = value

            # Increase frequency
            self.update_frequency(node)

            return

        # Cache full → evict LFU
        if self.size == self.capacity:

            """
            Example:

            min_freq = 1

            freq=1 list:
            2 <-> 5

            remove LRU = 2
            """

            lfu_list = self.freq_to_list[self.min_freq]

            node_to_remove = lfu_list.remove_lru()

            del self.key_to_node[node_to_remove.key]

            self.size -= 1

        # Create new node
        new_node = Node(key, value)

        self.key_to_node[key] = new_node

        # Insert into freq=1
        self.freq_to_list[1].insert(new_node)

        # Reset min frequency
        self.min_freq = 1

        self.size += 1


# =====================================================
# Example
# =====================================================

cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))
# Output: 1

# Frequency:
#
# 1 -> freq 2
# 2 -> freq 1

cache.put(3, 3)

# Remove 2 (lowest frequency)

print(cache.get(2))
# -1

print(cache.get(3))
# 3
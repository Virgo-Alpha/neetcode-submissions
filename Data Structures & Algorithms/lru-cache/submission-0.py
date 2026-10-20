class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    """
    We can use a doubly linked list where key-value pairs are stored as nodes, with the least recently used (LRU) node at the head and the most recently used (MRU) node at the tail. Whenever a key is accessed using get() or put(), we remove the corresponding node and reinsert it at the tail. When the cache reaches its capacity, we remove the LRU node from the head of the list. Additionally, we use a hash map to store each key and the corresponding address of its node, enabling efficient operations in O(1) time.
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # pop the least used
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]            

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict() # keeps track of insertion order/updates
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # mark it as most recently used by moving it to the "end" of the order.
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # mark it as most recently used by moving it to the "end" of the order
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            # pop the Least Recently used
            self.cache.popitem(last=False)

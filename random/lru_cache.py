from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
            
        # Move the accessed key to the end to mark it as "recently used"
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If it exists, move to end to mark as recently used
            self.cache.move_to_end(key)
            
        self.cache[key] = value
        
        # If we exceeded capacity, pop the first item (least recently used)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Test case
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # returns 1 (key 1 is now most recent)
cache.put(3, 3)        # evicts key 2
print(cache.get(2))    # returns -1 (not found)
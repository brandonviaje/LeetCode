from collections import defaultdict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}         # key -> value
        self.recency = {}       # key -> timestamp
        self.time = 0           # global counter to track recency

    def get(self, key: int) -> int:
        if key in self.cache:
            self.time += 1
            self.recency[key] = self.time  # update last used time
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1                     # increment time

        if key in self.cache:
            # update value and timestamp
            self.cache[key] = value
            self.recency[key] = self.time
        else:
            if len(self.cache) >= self.capacity:
                # evict LRU key
                lru_key = min(self.recency, key=self.recency.get)
                del self.cache[lru_key]
                del self.recency[lru_key]

            # add new key to cache and recency
            self.cache[key] = value
            self.recency[key] = self.time

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Two hashmaps:
- 'cache' stores the key-value pairs.
- 'recency' stores the last access time (to track usage order).

To evict the LRU item:
- Find the key with the smallest timestamp in 'recency' and delete it.
- Update 'recency' on every get or put to reflect the most recent use.

put: O(N)
get: O(1)
"""
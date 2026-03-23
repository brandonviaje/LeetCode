from random import randint
class RandomizedSet:

    def __init__(self):
        self.vals = []        
        self.map = {} # map val to index

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.vals.append(val)
        self.map[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        # get old index of val getting deleted
        old_idx = self.map[val]
        lastVal = self.vals[-1]
        self.vals[old_idx], self.vals[-1] = self.vals[-1],self.vals[old_idx] # swap with last elem
        self.map[lastVal] = old_idx                               # update swapped vals index

        self.vals.pop()                                                      # delete val
        del self.map[val]                                                    # delete val in map

        return True
    def getRandom(self) -> int:
        randomIdx = randint(0, len(self.vals) - 1) # get random num
        return self.vals[randomIdx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
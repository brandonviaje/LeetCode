class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.num = []

    def insert(self, val: int) -> bool:
        # check if val is in hashmap
        if val in self.map:
            return False

        # else add to list then map val to index
        self.num.append(val)
        self.map[val] = len(self.num) - 1
        return True

    def remove(self, val: int) -> bool:

        if val not in self.map:
            return False 

        # grab index of val we are going to delete and swap with last elem in num
        index = self.map[val]
        lastVal = self.num[-1]
        self.num[index] = lastVal

        # update last values index
        self.map[lastVal] = index
        
        # delete last number in list and delete val from map
        self.num.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.num)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
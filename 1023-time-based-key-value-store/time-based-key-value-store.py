class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # map key and add the list of value, and corresponding timestamp of it
        self.keys[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        # parse values
        values = self.keys.get(key,[])

        l,r = 0,len(values)-1

        # binary search help what to return
        while l<=r:
            mid = (l+r) >> 1
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid -1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
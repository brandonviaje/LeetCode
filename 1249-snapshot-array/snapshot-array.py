class SnapshotArray:

    def __init__(self, length: int):
        # init array of length filled with 0s, create snap_id
        self.arr = [[[-1,0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id,val])

    def snap(self) -> int:
        self.snap_id += 1                             # increment snap_id to 1
        return self.snap_id - 1                       # return prev snap_id that we captured
        
    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.arr[index], [snap_id + 1]) - 1 # binary search the snap_id to get the index of it at the arr
        return self.arr[index][i][1] # return the value that was set at that time stamp

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

"""
constructor should initialize array like data structure with the given length. each element should be 0 at firsst

set: set element at index to val
snap: save array at current snap_id, maybe using a hashmap. return the snap_id - 1. then after that increment it.
get: return val at index at that current snapshot
"""
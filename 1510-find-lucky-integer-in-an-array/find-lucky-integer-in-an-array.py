class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        maxKey = 0

        for key,value in count.items():
            # if key is bigger than max key and freq is same set that as max
            if key > maxKey and key == value:
                maxKey = key

        if maxKey != 0:
            return maxKey
        else:
            return -1
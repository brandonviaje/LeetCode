class Solution:
    def findLucky(self, arr: List[int]) -> int:
        track = Counter(arr)
        maxNum = -1

        for num, freq in track.items():
            if freq == num and num > maxNum:
                maxNum = num

        return maxNum
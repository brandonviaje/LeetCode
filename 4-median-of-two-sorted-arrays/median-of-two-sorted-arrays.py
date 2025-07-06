class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedArr = []

        # push to heap
        for num in nums1:
            sortedArr.append(num)

        for num in nums2:
            sortedArr.append(num)

        sortedArr.sort() # n log n

        # use two heaps if even
        if len(sortedArr) % 2 == 0:
            firstHalf = sortedArr[:len(sortedArr)//2]
            firstHalf = [-n for n in firstHalf]
            secondHalf = sortedArr[len(sortedArr)//2:]
            heapq.heapify(firstHalf) # firstHalf is maxHeap
            heapq.heapify(secondHalf) # secondHalf is a min heap
            return (heapq.heappop(firstHalf) * -1 + heapq.heappop(secondHalf)) / 2
        else:
            return sortedArr[len(sortedArr)//2]


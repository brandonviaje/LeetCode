class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        we can use a max heap to pop the largest element k times
        """

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        result = 0

        # while max heap not empty and k > 0, pop from max heap
        while max_heap and k > 0:
            result = heapq.heappop(max_heap)
            k -= 1

        return -result
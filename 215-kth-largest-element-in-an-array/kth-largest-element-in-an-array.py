class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max heap
        nums = [-n for n in nums]
        heapq.heapify(nums)

        while k > 0:
            # pop from max heap k times
            result = heapq.heappop(nums) * -1
            k -= 1

        return result


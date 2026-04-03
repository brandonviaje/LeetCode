class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        one way we can do this is sort the array so that we can use ptrs to manipulate
        the closest target
        """

        nums.sort()
        cand = 0
        closest = float('inf')
        for i in range(len(nums)):
            l,r = i+1,len(nums)-1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if abs(three_sum - target) < closest:
                    closest = abs(three_sum - target)
                    cand = three_sum
                
                if three_sum > target:
                    r -= 1
                else:
                    l += 1
        
        return cand
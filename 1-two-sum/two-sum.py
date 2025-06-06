class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in count:
                return [count[diff],i]

            count[num] = i
        
        return []
        
        
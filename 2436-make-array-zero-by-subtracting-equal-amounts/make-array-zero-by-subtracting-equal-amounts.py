class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        target = [0] * len(nums)
        result = 0
        x = float('inf')

        # keep looping until we reach a 0 array look alike
        while target != nums:

               # capture the min number that isnt zero
            for num in nums:
                if num != 0:
                    x = min(x,num)      

            for i in range(len(nums)):
                # if its a non zero number, then perform the operation
                if nums[i] != 0:
                    nums[i] -= x

            result += 1
            # reset X
            x = float('inf')
        
        return result
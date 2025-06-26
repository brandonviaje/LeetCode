class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        result = 0
        longest = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] <= nums[i-1]:
                longest = 1
            else:
                longest += 1

            result = max(result,longest)

        return result


        """
        longest = 1
        result = 0
        [2,2,2,2,2]
           ^
        """
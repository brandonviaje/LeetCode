class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l,r = 0,len(nums)-1

        """
        [2,2,1]
         ^
             ^
        result = 2

        [4,1,2,1,2]
         ^
           ^
        result = 4

        XOR cancels out duplicate nums

        - a ^ a = 0
        - a ^ 0 = a,

        XORing all values leaves the number that appears once.
        """
        result = 0
        for num in nums:
            result ^= num

        return result
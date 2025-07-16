class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        [1,2,3,3,4]
               ^

        result = 3

        [1,n]
        length: n + 1

        (1) -> (2) ->(3) - >(4) -> (3)
        """
        nums.sort()
        result = nums[0]

        for i in range(1,len(nums)):
            if nums[i] == result:
                return result
            else:
                result = nums[i]
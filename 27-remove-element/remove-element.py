class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        [2,2,3,3]
             ^
             ^
        val = 3

        idea: overwrite the index if it has a val
        keep track of result too see how mch
        """

        result = 0
        ptr = 0 

        for i in range(len(nums)):
            if nums[i] != val:
                nums[i],nums[ptr] = nums[ptr],nums[i]
                ptr += 1
                result += 1
 
        return result
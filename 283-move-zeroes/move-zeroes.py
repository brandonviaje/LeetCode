class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        suboptimal: we build an array where we add all the non negative numbers and then add all the 0s after
        have a ptr keep track of the non-zero nums, and then swap , after fill the rest with zeros
        """

        zeros = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[zeros] = nums[zeros],nums[i]
                zeros += 1

        # pad remaining arr with zeros
        for j in range(zeros,len(nums)):
            nums[j] = 0
        
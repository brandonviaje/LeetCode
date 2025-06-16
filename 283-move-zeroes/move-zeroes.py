class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # create a pointer to insert non zeroes in order 
        insert_pos = 0

        for read in range(len(nums)):
            #if the non zero put it in place
            if nums[read] != 0:
                nums[insert_pos] = nums[read]
                insert_pos += 1

        #everything else from insert_pos should be 0
        for i in range(insert_pos,len(nums)):
            nums[i] = 0

        # T O(n) S O(1)
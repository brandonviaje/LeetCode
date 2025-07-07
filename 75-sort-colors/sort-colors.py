class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right = 0, len(nums)-1
        zeroes = 0


        """
        [0, 0, 1, 1, 2, 2]
               ^
                   ^
               ^

        [0,1,2]
           ^
           ^
           
           ^ 
        """

        while left <= right:
            pass
            if nums[left] == 0:
                nums[left],nums[zeroes] = nums[zeroes],nums[left]
                zeroes += 1
                left += 1
            elif nums[left] == 1:
                left += 1
            else:
                nums[right],nums[left] = nums[left],nums[right] 
                right -= 1
        
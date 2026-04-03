class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        brute force: just call a sort function O(nlogn)
        """
        
        """
        [0,0,1,1,2,2]
             ^
                 ^ 
               ^

        [1,0,2]
           ^
         ^
            ^

        [0,0,1,1,1,2,2]
             ^
                    ^
                    ^
        """
        l,r = 0,len(nums)-1
        zeros = 0

        while l <= r:
            if nums[l] == 2:
                nums[l],nums[r] = nums[r],nums[l]
                r -= 1
            elif nums[l] == 1:
                l += 1
            else:
                nums[l],nums[zeros] = nums[zeros],nums[l]
                zeros += 1
                l += 1

        

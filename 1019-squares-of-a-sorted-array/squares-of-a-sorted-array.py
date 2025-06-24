class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #make them non negative
        for i,num in enumerate(nums):
            if num < 0:
                nums[i] *= -1

        nums.sort()

        left = 0
        right = len(nums) - 1
        while left<=right:
            if(left == right):
                nums[left] = nums[left]**2
                break
            nums[left] = nums[left]**2
            nums[right] = nums[right] **2
            left +=1 
            right -=1
        return nums        
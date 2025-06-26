class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        [1,0,2]
         ^ ^
           ^

        """
        left, right = 0, len(nums)-1
        current = 0
        while current <= right:
            if nums[current] == 0:
                nums[left],nums[current] = nums[current],nums[left]
                left += 1
                current += 1
                print(nums)
            elif nums[current] == 1:
                current += 1
            else:
                nums[right],nums[current] = nums[current], nums[right]
                right -= 1
      
     
                        
    
        
        
        
        
        
        
        
        
        
        """
        
        for i in range(len(nums)):
            left = nums[i]
            right = nums[len(nums)-i-1]
            
            if left == 2 and right == 2:
                if
            
                
                6-0-1=5
                6-1-1=4
                6-2-1=3
                
                
        [2, 1, 2, 0, 1, 2]
        [1, 1, 2, 0, 2, 2]

        """
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        BRUTE FORCE: save the last element to put at the first spot then 
        shift everything to the right and overwrite the first elem
        do it k times using a for loop

        [1,2,3,4,5,6,7]
                    ^
                 ^

        [7,6,5,4,3,2,1]

        [99,3,-100,-1]

        temp = 7

        REVERSE THE ARRAY
        THEN REVERSE  first k elements
        AFTER REVERSE last  n-k elements
        """
        
        n = len(nums)
        k %= n # normalize to prevent out of bounds error

        def reverse(l,r):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1

        
        reverse(0,n-1) # reverse entire array first
        reverse(0,k-1) # reverse first k elements
        reverse(k,n-1) # reverse k-n elements
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        """
        peak elem: an element > neighbors

        [1,3,4,2]
         ^
                ^
            ^
        output: 2

        intuition:
        start with binary search, if one neighbor is bigger than the current index, update pointer to check that side as it can be a peak element
        also have to check the first and last elem, since it only has one neighb to prevent IOB error
        """
        if len(nums) == 1:
            return 0
            
        # check first and last index
        if(nums[0] > nums[1]):
            return 0

        if(nums[len(nums)-1] > nums[len(nums)-2]):
            return len(nums)-1

        # start binary search
        l,r = 1,len(nums)-2

        while l <= r:
            mid = (l+r)//2

            # check neighbors
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid + 1]: # if right neighb is bigger, right neighb could be peak elem
                l = mid + 1
            else:                           # if left neighb is bigger, left neighb could be peak elem
                r = mid - 1

        return -1

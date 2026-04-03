class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
                           ^ 
             
        0 <= 1 <= 2, it would be on the left side
        if it isn't between the intervals, then it would be on the right side then

        if nums[mid] <= target <= nums[right], explore the right side of arr
        if nums[left] <= target <= nums[mid], explore the left side
        if nums[l] == nums[mid] == nums[r], cant determine which half is sorted, so u lose the ability to discard half the search space

        target = 6
        brute force sol: convert to a set, then membership check

        array can be rotated in many ways, but the left side of the array is gonna have larger or equal values than the right side
        [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1] hides the pivot since they're all duplicates, we should shrink the search space
        """

        l,r = 0,len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return True

            # shrink search space if duplicates
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            # check if left side is sorted
            elif nums[l] <= nums[mid]:
                # check if target is in the sorted half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # right half is sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False
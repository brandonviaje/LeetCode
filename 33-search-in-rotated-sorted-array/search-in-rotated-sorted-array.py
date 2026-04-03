class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        check which side of the array is sorted
        if its the left side, check if ur target resides in left side, if it does then search left side else search right
        
        if left side isn't sorted, then right side must be sorted so u check if ur target resides in the right side,
        if it does then search right side more else search left
        """


        result = -1
        l,r = 0,len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                result = mid
                return result

            # check if left side is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return result
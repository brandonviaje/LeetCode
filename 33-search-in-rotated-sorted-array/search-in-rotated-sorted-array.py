class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums)-1

        while l <= r:
            mid = (l+r)//2

            # if nums at middle is target return
            if nums[mid] == target:
                return mid

            # check if left side is sorted
            if nums[l] <= nums[mid]:
                # check if its in the left side else we explore the right

                # check if it is in the range of the left, if it isn't then it must be in the right side
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else: # else it must be in the left side, update right pointer
                    r = mid - 1
            else:
                # check if target is in the right side of the array, if it isnt, it must be on the left side
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: # else it must be in the right side, update left pointer
                    l = mid + 1

        return -1

        # T O(logn) S O(1)
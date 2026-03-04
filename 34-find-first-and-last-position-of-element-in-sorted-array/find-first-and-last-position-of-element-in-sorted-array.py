class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, -1
        l,r = 0,len(nums)-1

        # find the first position first
        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                left = mid # store as potential leftmst occurence of number
                r = mid - 1 # update ptr to search the left side to check if there is leftmost occurence
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l,r = 0,len(nums)-1

        # do a second binary search to find the rightmost occurence of the target
        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                right = mid # store potential rightmost index
                l = mid + 1 # explore the right side of the array to find the rightmost
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [left,right] if left != -1 and right != -1 else [-1,-1]


    """
    [5,7,7,8,8,10]
           ^
                ^
    target = 8

    [1]
     ^
     ^

    [0,0]

    T O(log n)
    S O(1)
    """
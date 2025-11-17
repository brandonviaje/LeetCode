class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        must run in logn, binary search implied
        - you are also given a sorted array, so binary search will help to eliminate search space

        when you get a number==target, you need to check if its the first occurence (leftmost index) of that num
           
        we can do a a two pass binary search:
        1. first binary search is to get the very first occurence (leftmost) of the target index
        2. second is to get very last index of the target num

        first BS + second BS:  logn + logn = O(logn)

        [5,7,7,8,8,10]
               ^
                    ^

        0 + 5 // 2 = 2
        7 // 2 = 3

        8 // 2 = 4
        """

        def leftMost():
            l, r = 0, len(nums)-1
            left = -1

            while l<=r:
                mid = (l+r)//2
                # tighten lower bound
                if nums[mid] >= target:
                    r = mid -1
                else:
                    l = mid + 1
                if nums[mid] == target:
                    left = mid

            return left

        def rightMost():
            l, r = 0, len(nums)-1
            right = -1

            while l<=r:
                mid = (l+r)//2
                # tighten upper bound
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
                if nums[mid] == target:
                    right = mid

            return right
        
        return [leftMost(), rightMost()]

        # T O(logn)
        # S O(1)
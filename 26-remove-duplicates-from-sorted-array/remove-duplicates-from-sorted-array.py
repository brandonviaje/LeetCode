class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        remove duplicates in place

        array is already sorted in increasing order

        we can have a set to keep track of membership,
        if it has already been seen in the set, dont add to result
        else add to result

        [1,2,2]
         ^
         ^

        [0,1,2,3,4,1,2,1,3,4]
                           ^
                   ^
         {0,1}
        """

        seen = set()
        unique = 0

        for i in range(len(nums)):
            # check if it is a duplicate
            if nums[i] in seen:
                continue
            
            # if not dupe, add to set swap val update ptr
            seen.add(nums[i])
            nums[i], nums[unique] = nums[unique], nums[i]
            unique += 1

        # get rid of duplicates
        for _ in range(len(nums) - unique):
            nums.pop()
        
        return len(nums)
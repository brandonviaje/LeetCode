class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        find all target indices of nums
        target index is an index i such that nums[i] == target

        there could be another target index on the right, so we would have to check that, 
        if there isnt anything on the right side, then we can safely search left

        brute force: sort the array, and iterate using a for loop and build result like that.
        this will make the result list have target indices in order
        """

        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        return result
        
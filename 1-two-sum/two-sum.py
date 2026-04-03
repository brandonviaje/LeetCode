class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        given an array nums, and a target
        need to return indices of two nums s.t. they add up to target

        a brute force way to do this is using two loops to check each pair and combination
        this would give us an O(n^2) TC

        another way to do this is by subtracting the current number by the target, 
        and check if the diff between the two nums are already seen in the hashmap
        """

        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]
            
            seen[nums[i]] = i

    
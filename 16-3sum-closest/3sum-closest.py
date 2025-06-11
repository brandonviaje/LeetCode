class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # O (nlogn) 
        nums.sort()
        closest = float('inf')

        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]
        #O(n^2)
        for i in range(len(nums)-2):
            #skip dupes to improve performance
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left = i + 1
            right = len(nums) - 1


            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                diff = abs(target - threeSum)
                # if the difference is less than the previous sum's difference
                if diff < abs(closest - target):
                    closest = threeSum #set it to be the new one

                #shift pointers based on the magnitude of threeSum
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    return threeSum
            
        return closest

        # T O(n^2) S O (1)
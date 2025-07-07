class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        [-4, -1, 1, 2]
          ^
                 ^       
                    ^

        sum = -1

        """
        nums.sort()
        diff = float('inf')
        closest = 0
        for i in range(len(nums)):
            # avoid dupes
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums)-1
            
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]

                if abs(threeSum - target) < diff:
                    diff = abs(threeSum - target)
                    closest = threeSum
                
                if threeSum == target:
                    return threeSum
                elif threeSum > target:
                    right -= 1
                else:
                    left += 1

        return closest
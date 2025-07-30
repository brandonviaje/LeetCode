class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        [-4,-1,1,2]
             ^
               ^
                  ^

        target: 1
        diff = 2
        res = -3
        sum: -3

        - find the smallest sum of the three numbers that are closest to the target
        - that means you need to use the smallest difference of the threeSum and target and keep updating it like that
        - three pointers to scan through the array, but should sort it first so that we can update pointers accordingly
        """
        nums.sort()
        result = 0
        prevDiff = float('inf')

        for i in range(len(nums)):
            l,r = i + 1, len(nums)-1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                
                if abs(target-threeSum) < prevDiff:
                    prevDiff = abs(target-threeSum)
                    result = threeSum

                if threeSum > target:
                    r -= 1
                else:
                    l += 1

        return result 
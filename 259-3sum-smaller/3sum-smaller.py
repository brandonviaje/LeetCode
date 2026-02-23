class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        """
        [-2,0,1,3]
          ^
            ^   
                 ^
        """
        nums.sort()
        n = len(nums)
        result = 0

        for i in range(n-2):
            l,r = i + 1, n-1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                # if three sum < target 
                if three_sum < target:
                    result += r - l # add the entire current window since everything else in between that is < target
                    l += 1
                else:
                    r -= 1

        return result

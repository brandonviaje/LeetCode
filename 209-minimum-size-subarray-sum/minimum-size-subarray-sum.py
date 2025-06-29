class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        l = 0
        add = 0

        for r in range(len(nums)):
            # expand window first
            add += nums[r]
            # shrink window if >= target
            while add >= target:
                result = min(result,r-l+1)
                add -= nums[l]
                l += 1

        return 0 if result == float('inf') else result

        """
        [2,3,1,2,4,3]
                 ^
                   ^
         add = 7
         target = 7
         result = 2

         shrink window if add >= target
         expand if < target
         T O(n) S O(n)
        """
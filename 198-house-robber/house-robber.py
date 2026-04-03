class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        cannot rob adjacent houses 

        states:
        - rob current house
        - skip current house

        DP[i] the max amount of money you can rob without alertin popo
        DP[i] = max(nums[i] + DP[i-2], DP[i-1])
        DP[i] = 0 if i > len(nums)
        """

        DP = [0] * (len(nums) + 2)

        for i in range(len(nums)-1,-1,-1):
            # base case
            if i == len(nums)-1:
                DP[i] = nums[i]

            DP[i] = max(nums[i] + DP[i+2], DP[i+1])

        return DP[0]
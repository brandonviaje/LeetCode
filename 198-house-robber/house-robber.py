class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        intuition:
        - you have to make the best choice when robbing a house
        - check if you should rob this house or skip it
        - if you rob it, you add nums[i] to the best result from i-2 (you can’t rob two in a row)
        - if you skip it, just take the result from i-1
        - you’re always asking: which one gives more money
        - you build up this decision for each house
        - dp[i] = the max money you can rob up to house i
        - tabulation: solve small subproblems,and use them to solve the bigger one 
        """

        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        # build the table
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        # fill the current dp index with the best choice, either skipping the house or robbing it.
        # start at the second index so u can do the adjacent check after
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1] # return the last val, which gives u the biggest result

        # T O(n) S O(n)
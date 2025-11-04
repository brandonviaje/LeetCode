class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        structure of problem reminds me of MCM DP solution. need to find the optimal split point to maximize coins

        you multiply values on the left side and right side of a specific balloon and try to maximize the cost

        let DP[i][j] be the max coins you can get popping balloons from i to j
        coins from left side  = dp[i][k]
        coins from right side = dp[k][j]
        coins from bursting k = nums[i] * nums[k] * nums[j]

        base case 
        dp[i][j] = 0 when i + 1 == j, no balloons between i and j
        """

        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}

        def DP(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            # no balloons between i and j
            if i + 1 == j:
                return 0

            max_coins = 0

            # choose k as last balloon to burst
            for k in range(i + 1, j):
                coins = DP(i, k) + nums[i] * nums[k] * nums[j] + DP(k, j)
                max_coins = max(max_coins, coins)

            memo[(i,j)] = max_coins
            return memo[(i,j)]

        return DP(0,n-1)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def DP(index):
            if index in memo:
                return memo[index]

            if index > n:
                return 0

            if index == n:
                return 1

            memo[index] = DP(index + 1) + DP(index + 2)
            return memo[index]

        return DP(0)
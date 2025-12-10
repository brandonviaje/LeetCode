class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        there are only two ways to climb to the top:

        1. 1 step
        2. 2 step

        basically
        """
        memo = {}
        def dp(num):
            if num in memo:
                return memo[num]

            if num > n:
                return 0

            if num == n:
                return 1

            memo[num] = dp(num + 1) + dp(num+2)  
            return memo[num]
            
        return dp(0)
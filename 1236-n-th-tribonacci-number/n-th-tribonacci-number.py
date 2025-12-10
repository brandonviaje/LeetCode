class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def DP(index):
            if index in memo:
                return memo[index]

            if index == 0:
                return 0

            if 0<index<=2:
                return 1

            memo[index] = DP(index-3) + DP(index -2) + DP(index -1)
            return memo[index]

        return DP(n)
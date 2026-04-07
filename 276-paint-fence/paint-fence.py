class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        - n fence posts and k colors.
        - each post must be painted one color.
        - cannot have 3 or more consecutive posts with the same color.

        return number of valid ways to paint the fence.

        let DP[i] = number of ways to paint i posts.

        base cases:
        - DP[1] = k (first post can be any of k colors)
        - DP[2] = k * k (second post can be same or different color)

        recurrence:
        - If the i-th post is different from (i-1):
            → (k - 1) choices * DP[i-1]

        - If the i-th post is same as (i-1):
            → must ensure (i-1) != (i-2)
            → (k - 1) choices * DP[i-2]

        DP[i] = (DP[i-1] + DP[i-2]) * (k - 1)
        """

        memo = {}

        def DP(index):
            # check if precomputed
            if (index) in memo:
                return memo[(index)]

            # base cases
            if index == 1:
                return k
            
            if index == 2:
                return k * k

            memo[index] = (DP(index-1) + DP(index-2)) * (k-1) # recurrence relation

            return memo[index]
        
        return DP(n)
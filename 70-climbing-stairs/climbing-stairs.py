class Solution:
    @lru_cache(maxsize = None)
    def climbStairs(self, n: int) -> int:
        # base case
        if n <= 1:
            return 1

        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
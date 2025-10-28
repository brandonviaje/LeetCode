import math

class Solution:
    def numSquares(self, n: int) -> int:
        # build list of all perfect squares <= n
        perfectSquares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        memo = {}

        def DP(num):
            # base case
            if num == 0:
                return 0
            if num < 0:
                return float('inf')

            # check if subproblem computed
            if num in memo:
                return memo[num]

            best = float('inf')
            
            for square in perfectSquares:
                best = min(best, 1 + DP(num - square))

            memo[num] = best
            return best

        return DP(n)

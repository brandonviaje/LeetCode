class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        memo = {}
        def DP(i, remain):
            # base cases
            if remain <= 0:
                return 0
            if i == n:
                return float("inf")
            # check if alreayd precomputed
            if (i,remain) in memo:
                return memo[(i,remain)]

            # check if you should paint current wall, or skip it and paint next wall
            memo[(i,remain)] = min(cost[i] + DP(i + 1, remain - 1 - time[i]), DP(i+1,remain))

            return memo[(i,remain)]

        return DP(0,n)

            
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
        want to explroe the different costs of each color of a house, and get the min cost

        subproblem:
        - take the current cost of house and color
        - explore next house based on this color
        """
        memo = {}
        n = len(costs)
        k = len(costs[0])

        def DP(house,color):
            # check if precomputed already
            if (house,color) in memo:
                return memo[(house,color)]

            if house == n:
                return 0
            
            result = float('inf')
            # explore each color
            for col in range(k):
                # skip same color
                if col == color:
                    continue
                # recurrence relation
                temp = costs[house][col] + DP(house+1,col)
                result = min(result, temp)
                memo[(house,color)] = result

            return memo[(house,color)]

        return DP(0,-1)
                
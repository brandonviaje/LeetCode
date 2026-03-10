class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
        given a cost matrix where cost[i][j] represents cost to paint house i with color j
        we want to return the min cost to paint all houses with different colors. no two houses can have the same
        adjacent color. 

        options:
        - can either paint current house current color
        - skip current house and paint same color
        - paint current house a different color
        - skip current house and paint next house different color
        """
        n = len(costs)
        k = len(costs[0])
        memo = {}

        def DP(house,color):
            # check if precomputed already
            if(house,color) in memo:
                return memo[(house,color)]

            # base case
            if house == n:
                return 0

            result = float('inf')
            
            # go through every diff color than prev
            for i in range(k):
                # skip same color
                if i == color:
                    continue

                # add current cost and explore the next house
                temp = costs[house][i] + DP(house+1,i)
                result = min(result, temp) # capture min cost to paint houses diff colors
                memo[(house,color)] = result

            return memo[(house,color)]
                
        return DP(0,-1) # start at house 0, -1 for curr color so u can explore first color
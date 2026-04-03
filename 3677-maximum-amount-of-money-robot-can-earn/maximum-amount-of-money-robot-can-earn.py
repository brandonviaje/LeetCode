class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        """
        robot can neutralize robbers in at most 2 cells on its path

        if coins[i][j] >= 0, add to total and explore the other paths
        if coins[i][j] < 0 and no more abilities, then they steal from the robots stash stash - abs(coins[i][j])

        MLE:

                if not coins:
            return 0

        memo = {}
        m,n = len(coins), len(coins[0])

        def DP(row,col,abilities):
            # base cases
            if row >= m or col >= n:
                return float('-inf')
            if row == m-1 and col == n-1:
                # check if we can neutralize final cell
                if coins[row][col] < 0 and abilities > 0:
                    return 0
                return coins[row][col]

            if (row,col,abilities) in memo:
                return memo[(row,col,abilities)]

            result = float('-inf')
            if coins[row][col] >= 0:
                result = coins[row][col] + max(DP(row+1,col,abilities), DP(row,col+1,abilities))
            else:
                # check if we can neutralize cell
                if abilities > 0:
                    result = max(DP(row+1,col,abilities-1), DP(row,col+1,abilities-1))
                
                # take max of gettin robbed or using ability
                result = max(result, coins[row][col] + DP(row+1,col,abilities), coins[row][col] + DP(row,col+1,abilities)) 

            memo[(row,col,abilities)] = result
            return memo[(row,col,abilities)]

        return DP(0,0,2)
        """

        m,n = len(coins), len(coins[0])
        dp = [[[float('-inf')] * 3 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                for k in range(3):
                    # base case
                    if row == m - 1 and col == n - 1:
                        take_hit = coins[row][col]
                        use_ability = float('-inf') 
                        # check if we can neutralize final cell if negative val
                        if (k > 0 and coins[row][col] < 0):
                            use_ability = 0

                        dp[row][col][k] = max(take_hit, use_ability)
                        continue

                    best_next = max(dp[row + 1][col][k], dp[row][col + 1][k])

                    # if positive add 
                    if coins[row][col] >= 0:
                        dp[row][col][k] = coins[row][col] + best_next
                    else:
                        take_hit = coins[row][col] + best_next
                        use_ability = float('-inf')

                        # get max of using ability or gettin robbed
                        if k > 0:
                            use_ability = max(dp[row+1][col][k-1], dp[row][col+1][k-1])

                        dp[row][col][k] = max(take_hit, use_ability)

        return dp[0][0][2]
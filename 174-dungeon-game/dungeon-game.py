class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """

        

        if we want to find the minimum initial health, starting from (0,0) is bad 
        Some paths might take huge damage early, and some might take less.

        u would need to consider all paths and track the minimum initial health over all paths, which is messy.

        change POV: if im at i,j what is the minimum amount of health i needed to save the princess

        what is the subproblem?

        p[i,j]=max(1,min(dp[i+1,j],dp[i,j+1])−dungeon[i,j])
        """

        # build from bottom up, tabulation

        m,n = len(dungeon), len(dungeon[0])

        dp = [[float('inf') for j in range(n+1)] for _ in range(m+1)]
        # set exit cell
        dp[m][n-1] = dp[m-1][n] = 1 

        # build from bottom up
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                # how much health you need to survive this cell
                need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(1, need)

        return dp[0][0]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        m*n grid

        grid[0][0] starting point
        grid[m-1][n-1] bottom right corner

        constraint: can only move down or right

        1 = obstacle
        0 = empty space

        find the unique possible paths

        bruteforce: backtracking discover all possible paths 
        optimal: cache the saved results which should improve the TC

        What is the overlapping subproblem? since we want to get to the end point grid[m-1][n-1], it is made up of a combination of paths
        Recurrence Relation: DP(i,j) = DP(i+1,j) + DP(i,j+1)
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @lru_cache(maxsize=None) # cache to store previously computed subproblems
        def dfs(row,col):

            # an obstacle, bounds check
            if row >= m or col >= n or obstacleGrid[row][col] == 1:
                return 0
            # we have found a path
            if (row,col) == (m-1,n-1):
                return 1

            # recurse to find all unique paths
            return dfs(row+1,col) + dfs(row,col+1)

        return dfs(0,0)

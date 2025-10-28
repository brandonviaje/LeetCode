class Solution:
    # Reccurence Relation: DP(i,j) = DP(i+1,j) + DP(i,j+1)
    """
    can only move down or right
    Let DP(i,j) be the number of possible unique paths to reach end
    DP(i,j) = DP(i+1,j) + DP(i,j+1)
    """
    
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def DFS(row,col):
            # check for precomputed solutions
            if (row,col) in memo:
                return memo[(row,col)]

            # check if reached goal
            if (row,col) == (m-1,n-1):
                return 1
            # base case, out of bounds
            if row >= m or col >= n:
                return 0

            # recurrence relation
            memo[(row,col)] = DFS(row+1,col) + DFS(row,col+1)
            return memo[(row,col)]

        return DFS(0,0)
class Solution:
    # Reccurence Relation: DP(i,j) = DP(i+1,j) + DP(i,j+1)
    
    def uniquePaths(self, m: int, n: int) -> int:
        # Cache result of subproblems to better the TC
        @lru_cache(maxsize = None)
        def dfs(row,col):
            # Out of bounds check
            if row >= m or col >= n:
                return 0

            # We have found a unique path
            if (row,col) == (m-1,n-1):
                return 1

            # Explore down or right
            return dfs(row+1,col) + dfs(row,col+1)

        return dfs(0,0)
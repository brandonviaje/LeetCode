class Solution {
public:
    int DP(int r, int c, vector<vector<int>>& grid, vector<vector<int>>& memo) {

        int m = grid.size();
        int n = grid[0].size();

        // base case
        if(r >= m || c >= n || grid[r][c] == 1) return 0;
        if(r == m-1 && c == n-1) return 1;
        
        // check if sol precomputed
        if(memo[r][c] != -1) return memo[r][c];

        memo[r][c] = DP(r+1,c,grid,memo) + DP(r,c+1,grid,memo); // recurrence relation

        return memo[r][c];
    }

    int uniquePathsWithObstacles(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> memo(m, vector<int>(n, -1));

        return DP(0,0,grid,memo);
    }
};
class Solution {
public:
    vector<int> dx = {-1,0,1,0}, dy = {0,1,0,-1};

    // DFS
    int DFS(int row, int col, vector<vector<int>>& grid)
    {
        grid[row][col] = 0;
        int area {1};

        for(int i {}; i< 4; i++)
        {
            int nr = row + dx[i];
            int nc = col + dy[i];

            // check error out of bounds, and if if neighb cell is land
            if(nr >= 0 && nr<grid.size() && 0<=nc && nc<grid[0].size() && grid[nr][nc] == 1)
            {
                area += DFS(nr,nc,grid); // recurse further 
            }
        }

        return area;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int result {};
        for(int i {}; i < grid.size(); i++)
        {
            for(int j {}; j < grid[0].size(); j++)
            {
                // run a DFS if we encounter an island
                if(grid[i][j] == 1)
                {
                    result = std::max(result, DFS(i,j,grid));
                }
            }
        }
        return result;
    }
};
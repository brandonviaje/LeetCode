class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if(obstacleGrid.empty() || obstacleGrid[0][0] == 1)
        {
            return 0;
        }

        const int ROWS = obstacleGrid.size();
        const int COLS = obstacleGrid[0].size();
        vector<int> dp(COLS,0);
        dp[0] = 1;

        for(int i{}; i < ROWS; i++)
        {
            for(int j{}; j < COLS; j++)
            {
                if(obstacleGrid[i][j]==1)
                {
                    dp[j] = 0;
                }
                else{
                    if(j > 0)
                    {
                        dp[j] += dp[j-1];
                    }
                }
            }
        }

        for(int num : dp)
        {
            std::cout << num << '\n';
        }
        
        return dp[COLS-1];
    }
};
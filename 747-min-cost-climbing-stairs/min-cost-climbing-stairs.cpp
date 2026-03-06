class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        /*
        *
        *  should keep track of a cost val
        *
        *
        */
        std::unordered_map<int,int> memo;
        return min(DP(0,cost,memo), DP(1,cost,memo));
    }

    int DP(int n, vector<int>& cost, std::unordered_map<int,int>& memo)
    {
        if(memo.count(n)) return memo[n];

        // check if we reached top of staircase
        if(n >= cost.size())
        {
            return 0;
        }

        memo[n] = min(cost[n] + DP(n + 1, cost, memo), cost[n] + DP(n+2, cost,memo)); // get min cost of moving 1 step and 2 step

        return memo[n];
    }
};
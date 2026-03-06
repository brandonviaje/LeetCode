class Solution {
public:
    int numSquares(int n) {
        vector<int> squares;
        std::unordered_map<int,int> memo;

        for(int i {1}; i*i <= n; i++)
        {
            squares.push_back(i*i);
        }

        return DP(n,squares,memo);
    }

    int DP(int num, vector<int>& squares, std::unordered_map<int,int>& memo)
    {
        int min_cost = INT_MAX;
        if(num == 0) return 0;

        if(memo.count(num)) return memo[num];

        for(int square : squares)
        {
            if(num - square >= 0)
            {
                min_cost = min(min_cost, 1 + DP(num-square, squares, memo));
            }
        }

        return memo[num] = min_cost;
    }
};
class Solution {
public:
    int DP(int n, std::unordered_map<int,int>& memo)
    {
        // base cases
        if(n == 0)
        {
            return 0;
        }

        if(n<=2)
        {
            return 1;
        }

        // check precomputed
        if(memo.find(n) == memo.end())
        {
            memo[n] = DP(n-3,memo) + DP(n-2,memo) + DP(n-1,memo);
        }

        return memo[n];
    }
    int tribonacci(int n) {

        std::unordered_map<int,int> memo;
        return DP(n,memo);
        
    }
};
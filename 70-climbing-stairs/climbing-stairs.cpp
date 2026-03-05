class Solution {
public:
    int DP(int n, unordered_map<int,int>& memo) {
        // base case
        if (n == 0 || n == 1) {
            return 1;
        }

        // check for precomputed solution
        if (memo.find(n) == memo.end()) {
            memo[n] = DP(n-1, memo) + DP(n-2, memo);
        }

        return memo[n];
    }

    int climbStairs(int n) {
        unordered_map<int, int> memo;
        return DP(n, memo);
    }
};
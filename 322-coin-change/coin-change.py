class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Greedy approach: choose the biggest coin first until you cant anymore,
        then choose the second biggest coin and so on.

        we need a counter to keep track of it.

        Subproblem:

        - We can either take the coin or don't

        If coin + sum > amount:
        - Don't Take it, move onto next coin

        If coin + sum < amount:
        - Don't Take it, move onto next coin
        - Take the coin, keep taking the same coin


        Let T[n,b] be the minimum number of coins needed to make up that amount
        T[n,b] = min(T[n,b - v_n], T[n+1,b])

        Take the minimum of those two options


        Base cases:
        - If the amount is 0, you can take 0 coins
        - If the running total is greater than the sum, return -1
        - If there are no coins, then you can't make up the amount, return -1
        """
        memo = {}
        def DP(index, curr_sum):
            #if already pre computed
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            # base cases
            if curr_sum == 0:
                return 0
            if curr_sum < 0 or index >= len(coins):
                return float('inf') # impossible

            # recurrence relation: take same coin, or don't take coin and skip to next
            memo[(index, curr_sum)] = min(1 + DP(index, curr_sum - coins[index]), DP(index+1, curr_sum))    
            return memo[(index, curr_sum)]

        result = DP(0,amount)
        return -1 if result == float('inf') else result
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        You can choose to buy a stock on a certain day, or skip.
        You can choose to sell a stock on a certain day, or skip.
        
        The goal is to maximize total profit — you can make as many transactions 
        as you want

        Whenever today's price is higher than yesterday's, we can treat that as 
        part of a profitable transaction, effectively capturing all upward trends.

        Dynamic Programming Intuition:
        - dp[i][0]: max profit on day i when not holding a stock
        - dp[i][1]: max profit on day i when holding a stock
        """

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit
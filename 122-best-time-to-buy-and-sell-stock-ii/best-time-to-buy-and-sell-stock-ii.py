class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # start at 1 to prevent out of bounds error
        for i in range(1, len(prices)):
            # if current price is greater than prev day
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1] # add profit for those two
        
        return profit
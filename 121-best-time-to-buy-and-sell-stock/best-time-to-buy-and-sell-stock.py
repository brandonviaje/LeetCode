class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price-minPrice

        return maxProfit
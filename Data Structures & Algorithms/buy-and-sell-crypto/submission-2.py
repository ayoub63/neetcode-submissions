class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sell = prices[1]
        max_profit = 0
        for i in range(0, len(prices)):
            max_sell = max(max_sell, prices[i])
            max_profit = max(max_profit, max_sell - prices[i])

        
        return max_profit
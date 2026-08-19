class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for i in range(0, len(prices)):
            min_buy = min(min_buy, prices[i])
            max_profit = max(max_profit, prices[i] - min_buy)

        
        return max_profit if max_profit > 0 else 0
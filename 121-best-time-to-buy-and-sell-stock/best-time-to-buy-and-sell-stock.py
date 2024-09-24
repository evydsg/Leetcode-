class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, left = 0, 0

        for index, price in enumerate(prices):
            while prices[left] > price:
                left += 1
            
            maxProfit = max(maxProfit, price - prices[left])
        
        return maxProfit
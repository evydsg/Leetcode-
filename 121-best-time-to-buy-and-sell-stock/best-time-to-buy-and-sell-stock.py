class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, index = 0, 0
        maxProfit = 0

        while index < len(prices):
            while prices[left] > prices [index]:
                left += 1
            
            maxProfit = max(maxProfit, (prices[index]- prices[left]))
            index += 1
        
        return maxProfit
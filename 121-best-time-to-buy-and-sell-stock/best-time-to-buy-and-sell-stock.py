class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        leftPtr, rightPtr = 0, 0

        while rightPtr < len(prices):
            while prices[leftPtr] > prices[rightPtr]:
                leftPtr += 1
            
            maxProfit = max(maxProfit, prices[rightPtr] - prices[leftPtr])
            rightPtr += 1
        
        return maxProfit
        
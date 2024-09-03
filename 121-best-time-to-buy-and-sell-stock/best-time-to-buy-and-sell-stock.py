class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Understand
                The idea is to find the maximum profit I have from buying a stock and later selling it 
                Thus to say that the day where we buy must have a lower price than the one we sell

                Can we have an empty array?
                Can we have an array with negative elements?
                Can we have duplicates?
            
            Match
                Sliding Window
            
            Plan
                Initialize a left pointer at the beginning of the array, variable to keep track of the maximum profit
                Iterate through the prices
                    Check if left pointer is less than the right pointer
                        if so, increment the left pointer
                    Calculate the maximum profit
                        profit = prices[right] - profit[left]
                    Update the profit to have the maximum profit found so far
            
            Evaluate
                Time Complexity: O(n)
                Space Complexity: O(1)
        """
        left_ptr, max_profit = 0, 0

        for index in range(len(prices)):
            while prices[left_ptr] > prices[index]:
                left_ptr += 1
            
            max_profit = max(max_profit, prices[index] - prices[left_ptr])
        
        return max_profit
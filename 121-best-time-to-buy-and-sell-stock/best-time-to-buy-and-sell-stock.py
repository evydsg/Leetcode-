class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Understand
                The idea is to calculate the day to buy in which the price is at it lowest and you can sell at highest

                Questions
                    Can we have an empty array?
                    Can we have an array with negative integers?
            
                Edge cases  
                    prices = [7,1,5,3,6,4]
                    price[0] = 7
                    price[-1] = 4

                    if price[left] > price[right]:
                        left += 1
                    if price[left] < price[right]:
                        max_profit = max(max_profit, profit)
                
            Match 
                Find minimum price
            
            Plan
                Check if list is empty
                    if len(prices) == 0:
                        return 0
                Initialize a variable to keep track of minimum price
                    min_price = float("inf")
                Initialize a variable to keep track of max profit
                    max_profit = 0
                Traverse through the list
                    for price in prices:
                    Check if current price is less than min_price
                    Calculate the profit 
                        profit = price - min_price
                    Update the profit to have the max_profit
                        max_profit = max(profit, max_profit)
                
            Evaluate    
                Time Complexity
                    O(n) since we traverse through the array 
                Space Complexity
                    O(1), we simply use one variable to keep track of the max price

        """
        if len(prices) == 0:
            return 0
        
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(price, min_price)

            profit = price - min_price

            max_profit = max(profit, max_profit)
        
        return max_profit

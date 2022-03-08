# 121. Best Time to Buy and Sell Stock

#method1 - One Pass - Time complexity - O(n)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = float('inf')
        max_profit =  0
        
        for i in range(len(prices)):
            
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i]-min_price
                
        return max_profit
        
        
#method2 : Brute Force Time complexity - O(n^2)

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit
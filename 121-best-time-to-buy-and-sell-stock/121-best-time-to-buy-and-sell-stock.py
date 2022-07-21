class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = None
        
        profit = 0
        
        
        
        for price in prices:
            if buy is None:
                buy = price
            
            if price < buy:
                buy = price
                
            profit = max(profit, price - buy)
                
                
            
        return profit
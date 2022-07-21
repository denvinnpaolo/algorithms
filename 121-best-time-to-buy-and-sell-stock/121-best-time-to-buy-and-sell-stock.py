class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = None
        
        profit = 0
        
        for price in prices:
            if buy is None:
                buy = price
            
            if price < buy:
                buy = price
                
            if profit < price - buy:
                profit = price-buy
                
                
            
        return profit
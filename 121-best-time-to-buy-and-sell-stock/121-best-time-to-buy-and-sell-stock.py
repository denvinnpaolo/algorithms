class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        mx = float('-inf')
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            
            mx = max(mx, prices[r] - prices[l])
            
        return mx
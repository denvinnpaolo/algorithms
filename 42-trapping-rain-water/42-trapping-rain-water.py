class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = height[0]
        rmax = height[-1]
        
        l,r = 0, len(height) - 1
        
        total = 0
        
        while l <= r:
            if height[l] > lmax:
                lmax = height[l]
                
            if height[r] > rmax:
                rmax = height[r]
                
            if lmax <= rmax:
                total += lmax - height[l]
                l += 1
            else:
                total += rmax - height[r]
                r -= 1
                    
        return total
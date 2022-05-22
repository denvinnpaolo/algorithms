class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        lmax = height[l]
        rmax = height[r]
        max_water = 0
        
        while l < r:
            if lmax < height[l]:
                lmax = height[l]
                
            if rmax < height[r]:
                rmax = height[r]
                
            h = min(lmax, rmax)
            
            lg = r - l

            pot = h*lg
            
            max_water = max(pot, max_water)
            
            if lmax < rmax:
                l += 1
            else:
                
                r -= 1
            
        return max_water
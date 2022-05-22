class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        lMax = height[0]
        rMax = height[-1]
        
        i = 0
        j = len(height) - 1
        
        while i < j:
            if lMax < height[i]:
                lMax = height[i]
            
            if rMax < height[j]:
                rMax = height[j]
            
            if lMax <= rMax:
                total += lMax - height[i]
                i += 1
            else:
                total += rMax - height[j]
                j -= 1
                
        return total
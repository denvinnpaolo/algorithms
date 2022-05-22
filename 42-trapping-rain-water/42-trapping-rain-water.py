# GOAL:
# list elements >= 0 
# unsorted array
# height >= 3

# input == list<int>
# output == max num of water trapped 

class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        
        left = 0
        right = len(height) - 1
        
        l_max = height[0]
        r_max = height[-1]
        
        while left < right:
            
            if l_max < height[left]:
                l_max = height[left]
                
            if r_max < height[right]:
                r_max = height[right]
                
            
            if l_max <=r_max:
                res += (l_max-height[left])
                left+= 1
            else:
                res+= (r_max-height[right])
                right -= 1
                
        return res
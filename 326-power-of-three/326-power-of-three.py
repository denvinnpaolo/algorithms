class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 1:
            return True
        base = 3
        
        while base < n:
            base *= 3
            
        if base == n:
            return True
        
        return False
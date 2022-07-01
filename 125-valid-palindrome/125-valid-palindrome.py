class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmedString = ""
        
        for c in s:
            if c.isalnum():
                trimmedString+= c.lower()
        l = 0
        r= len(trimmedString) - 1      
        
        while l <= r:
            if trimmedString[l] == trimmedString[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        
        return True
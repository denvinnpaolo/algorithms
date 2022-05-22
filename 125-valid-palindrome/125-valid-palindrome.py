class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        phrase = ""
        
        for char in s:
            if char.isalnum():
                phrase += char.lower()
        
        if len(phrase) == 0:
            return True
        
        l = 0 
        r = len(phrase) - 1
        
        while l < r:
            if phrase[l] == phrase[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True
        
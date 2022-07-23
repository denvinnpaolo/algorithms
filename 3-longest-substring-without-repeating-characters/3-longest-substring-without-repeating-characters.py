class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hi = 0
        sub = ""
        
        i = 0
        
        while i < len(s):
            if s[i] in sub:
                start = sub.index(s[i])
                sub += s[i]
                sub = sub[start + 1:]
            else:
                sub += s[i]
            
                
            if len(sub) > hi:
                hi = len(sub)
            i += 1
                
        return hi
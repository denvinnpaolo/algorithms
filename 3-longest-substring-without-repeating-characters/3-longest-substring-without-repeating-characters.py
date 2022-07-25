class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        hi = 0
        
        for c in s:
            if c in sub:
                start = sub.index(c)
                sub = sub[start + 1:]
            sub += c
            
            if len(sub) > hi:
                hi = len(sub)
                
        return hi
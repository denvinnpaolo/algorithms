class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hi = 0
        sub = ""
        
        for c in s:
            if c not in sub:
                sub += c
            else:
                start = sub.index(c)
                sub += c
                sub = sub[start + 1:]
            if len(sub) > hi:
                hi = len(sub)
                
        return hi
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        sub = ""
        
        for i in range(len(s)):
            if s[i] in sub:
                start = sub.index(s[i])
                sub += s[i]
                sub = sub[start + 1:]
            else:
                sub+= s[i]
            if len(sub) > longest:
                longest = len(sub)
                
        return longest
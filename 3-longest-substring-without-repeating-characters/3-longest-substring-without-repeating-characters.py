class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        sub = ""
        
        for i in range(len(s)):
            print(s[i])
            if s[i] in sub:
                start = sub.index(s[i])
                sub += s[i]
                sub = sub[start + 1:]
            else:
                sub+= s[i]
            if len(sub) > longest:
                longest = len(sub)
                
        return longest
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        \
        
        
        
        
        
        
        
        
        
        
        
        
#         total = 0
        
#         n = len(s)
        
#         for i in range(n):
#             temp = ''
#             for char in s[i:]:
#                 if char not in temp:
#                     temp += char
                
#                     if len(temp) > total:
#                         total = len(temp)
#                 else:
#                     break
#         return total
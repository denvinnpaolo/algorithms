class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
                
        for ch in t:
            if ch in d:
                d[ch] -= 1
                
                if d[ch] == 0:
                    del d[ch]
            else:
                d[ch] = 1
            
        print(d)
        return True if len(d) == 0 else False
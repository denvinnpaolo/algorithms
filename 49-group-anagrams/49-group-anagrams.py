class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            st = "".join(sorted(s))
            
            if st in d:
                d[st].append(s)
                
            else:
                d[st] = [s]
                
        return d.values()
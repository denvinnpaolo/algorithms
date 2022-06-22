class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        
        for st in strs:
            sorted_str = "".join(sorted(st))
            
            if sorted_str in d:
                d[sorted_str].append(st)
            else:
                d[sorted_str] =[st]
        
        vals = d.values()
        
        return list(vals)
# given two string input
# input must be same length
# inputs are anagrams if they contain same exact number of letters
# in anagrams, letters can be rearranged

# 2. check if len(s) == len(t)
# 1. check if s and t are type string
# 3. choose to iterate and append every char of either s or t to a hash table
# 4. if string has a letter that isn't in hash table or key == 0 then return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        di = {}
        
        # add letters to dict
        for c in s:
            if c in di:
                di[c] += 1
            else:
                di[c] = 1
        
        for c in t:
            if c in di:
                di[c] -= 1
                if di[c] == -1:
                    return False
            else:
                return False
        return True
                
            
        
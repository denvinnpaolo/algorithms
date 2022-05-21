# GOAL: return true if the input strings are anagrams of each other
# anagram is a word or phrase formed by rearranging the letters of a different word or phrase
# len(s) == len(t)
# inputs == type str
# output == bool


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        
        if len_s == 0 or len_t == 0 or len_s!= len_t:
            return False
        
        s_hash = dict()
        
        for letter in s:
            if letter in s_hash:
                s_hash[letter] += 1
            else:
                s_hash[letter] = 1
                
        for letter in t:
            if letter not in s_hash:
                return False
            elif s_hash[letter] == 0:
                return False
            else:
                s_hash[letter] -= 1
        return True
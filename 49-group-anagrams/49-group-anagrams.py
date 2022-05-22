# Goal: return a list of grouped anagrams
#  strs = unsorted list<str>
# 1 <= len(str) <= 10,000
# 0 <= len(strs) <= 100
# char in str == lower english letters

# input == list<str>
# output == list<list>

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_words = dict()
        
        for str in strs:
            sorted_str = sorted(str)
            
            word = "".join(sorted_str)
            
            if word in seen_words:
                seen_words[word].append(str)
            else:
                seen_words[word] = [str]
                
        grouped_anagrams = seen_words.values()
        
        return grouped_anagrams        
        
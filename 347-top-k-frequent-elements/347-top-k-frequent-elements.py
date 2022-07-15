class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
                
        sorted_d = reversed(sorted(d, key=lambda k: d[k]))
        
        return list(sorted_d)[:k]
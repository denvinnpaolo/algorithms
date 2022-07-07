class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        
        hi = 0
        
        for num in nums:
            cur = 1
            nxt = num + 1
            
            if num - 1 in s:
                continue
            else:
                while nxt in s:
                    cur += 1
                    nxt += 1
                
            if cur > hi:
                hi = cur
                
        return hi
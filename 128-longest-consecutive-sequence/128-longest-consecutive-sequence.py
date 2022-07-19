class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)     
        
        hi = 0
        cur = 0
        
        for i in range(len(nums)):
            cur = 1
            nxt = nums[i] + 1
            if nums[i] - 1 in s:
                continue
            else:
                while nxt in s:
                    nxt += 1
                    cur += 1
            
            if cur > hi:
                hi = cur
            
        return hi
                    
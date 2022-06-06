# GOAL: return the only missing number in the range
# postive int array
# [0...n] where 0 is always guranteed
# 10,000 > len(arr) > 0
# unsorted



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        
        for num in nums:
            s.add(num)
        
        for num in range((len(nums) + 1)):
            if num not in s:
                return num
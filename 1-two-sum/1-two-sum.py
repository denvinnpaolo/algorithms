# GOAL: return two indices in the array that sums up to target num
# return ascending indices
# not sorted
# 0 < len(nums) < 10,000
# el can be repeated
# one solution

# [0 1 8 1 7]
#  5

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for idx in range(len(nums)):
            potNum = target - nums[idx]
            
            if potNum in d:
                return [d[potNum], idx]
            else:
                d[nums[idx]] = idx
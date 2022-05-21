# GOAL: Scan the array to see if there are only one value for each element in the array.
# if a value is repeated return false else true
# input == list of int
# output == boolean
# maximum input = 10^5 (100,000)
# minimum input = 1

# element value is from -10^9 <= 10^9


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        passedVals = set([])
        
        for i in range(len(nums)):
            cur_val = nums[i]
            if cur_val in passedVals:
                return True
            
            passedVals.add(cur_val)
        
        return False
# int nums
# given a target
# must return indices of two numbers that add up to target
# there's always a solution within the array
# can't use same element twice but can use the same number

# steps
# 1. go through each number in nums
# 2. subtract num to target
# 3. check if number looking for was passed
# 4. continue until found

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: value
        # num: index
        d ={}
        
        
        for i in range(len(nums)):
            pot_num = target - nums[i]
            
            if pot_num in d:
                return [d[pot_num], i]
            else:
                d[nums[i]] = i
                
                
                
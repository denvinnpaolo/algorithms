# List of int num
# given a target num that is a sum of two int in the list
# there will always be number

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        d = {}
        
        for i in range(len(nums)):
            num = target - nums[i]
            
            if num in d:
                return [d[num], i]
            else:
                d[nums[i]] = i
        
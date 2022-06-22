class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        
        for i in range(len(nums)):
            num = target - nums[i]
            
            if num in d:
                return [d[num], i]
            else:
                d[nums[i]] = i
        
        print(d)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        
        for idx in range(len(nums)):
            pot_num = target - nums[idx]
            
            if pot_num in d:
                return [d[pot_num], idx]
            else:
                d[nums[idx]] = idx
            
            
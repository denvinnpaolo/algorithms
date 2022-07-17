import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = {}
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = numpy.prod(nums[:i] + nums[i + 1:])
        
        res = []
        
        for i in range(len(nums)):
            res.append(d[nums[i]])
            
        return res
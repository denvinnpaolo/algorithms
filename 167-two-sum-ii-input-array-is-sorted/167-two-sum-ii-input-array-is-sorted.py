class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            potNum = nums[right] + nums[left]
            
            if potNum == target:
                return [left+ 1, right+ 1]
            elif potNum > target:
                right -= 1
            else:
                left += 1
                
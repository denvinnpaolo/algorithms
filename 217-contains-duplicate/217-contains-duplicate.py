class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = set(nums)
        
        return len(checked) != len(nums)
# int array nums
# return true if num appears more than once else returns false
# array not sorted
# if empty return Null

# steps
# iterate through the array
# add value in a set
# if num in set return True
# if iteration finishes return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        
        return False
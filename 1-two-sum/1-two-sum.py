# key points
# - list not sorted
# - repeating elements
# - integer values
# - exactly one solution
# - Do not return same indices

# input == list<int>
# output == list<int> and len(list) == 2


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        
        for i in range(len(nums)):
            comp = target-nums[i]
            
            if comp in seen_nums:
                return [seen_nums[comp],i]
            else:
                seen_nums[nums[i]] = i
        
        print(seen_nums)
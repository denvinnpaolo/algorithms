class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            

            
            while left < right:
                potNum = nums[i] + nums[left] + nums[right]
                if potNum == 0:
                    ans = (nums[i], nums[left], nums[right])
                    res.add(ans)
                    right -= 1
                    left += 1
                elif  potNum > 0:
                    right -= 1
                else:
                    left += 1
        
    
        return res
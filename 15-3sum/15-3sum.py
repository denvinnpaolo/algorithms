class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets = set()
        ln = len(nums)
        
        for i in range(ln):
            l, r = i + 1, ln - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    triplet = (nums[i], nums[l], nums[r])
                    triplets.add(triplet)
                    l+= 1
                    r -= 1
                elif s > 0:
                    r-= 1
                else:
                    l += 1
        return triplets
            
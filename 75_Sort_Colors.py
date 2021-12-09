# Sort Colors

# Description:
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is 0, 1, or 2.


# Result
# Runtime: 32 ms, faster than 76.28% of Python3 online submissions for Sort Colors.
# Memory Usage: 14.3 MB, less than 46.90% of Python3 online submissions for Sort Colors.


# Solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                nums[s], nums[i] = nums[i], nums[s]
                s += 1
        
        for i in range(l):
            if nums[i] == 1:
                nums[s], nums[i] = nums[i], nums[s]
                s += 1
                
        
                
    
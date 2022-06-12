# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        hi = self.maxDepthHelper(root, 0, -1)
        
        return hi
        
    def maxDepthHelper(self, root, count, hi):
        if count > hi:
            hi = count
        
        if root == None:
            return hi
        
        hi = self.maxDepthHelper(root.left, count + 1, hi)
        hi = self.maxDepthHelper(root.right, count + 1, hi)
     
        return hi
        
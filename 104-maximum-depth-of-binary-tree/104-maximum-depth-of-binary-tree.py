# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.maxDepthHelper(root, 0, float('-inf'))
        
    def maxDepthHelper(self, node, lvl, hi):
        if lvl > hi:
            hi = lvl
            
        if node is None:
            return hi
        
        
        hi = self.maxDepthHelper(node.left, lvl + 1, hi)
        hi = self.maxDepthHelper(node.right, lvl + 1, hi)
        
        return hi
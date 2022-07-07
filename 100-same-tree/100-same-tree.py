# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = [True]
        
        def dfs(f, s):
            if not f and not s:
                return
            
            if f and s and (f.val == s.val):
                dfs(f.left, s.left)
                dfs(f.right, s.right)
            else:
                res[0] = False
        
        dfs(p, q)
        
        return res[0]
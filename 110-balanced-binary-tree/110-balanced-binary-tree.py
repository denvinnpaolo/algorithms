# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            print(abs(l-r) > 1)
            print(l, r)
            if abs(l-r) > 1:
                balanced[0] = False
            
            return max(l,r) + 1
        
        dfs(root)
        
        return balanced[0]
        
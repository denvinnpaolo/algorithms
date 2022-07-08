# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        b_vals  =[]
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            b_vals.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return b_vals[k -  1]
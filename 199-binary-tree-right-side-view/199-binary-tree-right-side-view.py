# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lvls = []
        
        
        
        def dfs(node, l):
            if not node:
                return
            
            if len(lvls) > l:
                lvls[l].append(node.val)
            else:
                lvls.append([node.val])
            
            dfs(node.left, l + 1)
            dfs(node.right, l + 1)
                
        dfs(root, 0)
        res = []
        for lvl in lvls:
            res.append(lvl[-1])
        
        return res
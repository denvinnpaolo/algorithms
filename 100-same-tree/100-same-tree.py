# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first = self.preorder(p, [])
        second = self.preorder(q, [])
        
        
        if first == second:
            return True
        
        return False
    
    def preorder(self, root, res):
        if root == None:
            res.append(None)
            return res
        
        res.append(root.val)
        
        res = self.preorder(root.left, res)
        res = self.preorder(root.right, res)
        
        return res
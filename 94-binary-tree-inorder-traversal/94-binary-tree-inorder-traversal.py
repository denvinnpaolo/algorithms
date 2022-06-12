# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = self.inorderHelper(root, [])
        
        return res
        
    def inorderHelper(self, root, res):
        if root == None:

            return res
        
        res = self.inorderHelper(root.left,res)
        res.append(root.val)
        res = self.inorderHelper(root.right,res)
        
        return res
        
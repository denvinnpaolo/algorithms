# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = self.postorderHelper(root, [])
        
        return res
        
    def postorderHelper(self, root, res):
        if root == None:
            return res
        
        res = self.postorderHelper(root.left, res)
        res = self.postorderHelper(root.right, res)
        
        res.append(root.val)
        
        return res
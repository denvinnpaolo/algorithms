# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        res = self.preorderHelper(root, res)
        
        return res
        
        
        
    def preorderHelper(self,root, res):
        if root == None:
            return res

        res.append(root.val)

        res = self.preorderHelper(root.left, res)
        res = self.preorderHelper(root.right, res)
        
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = self.preorder(root, 1, [])
        
        return res
        
    def preorder(self, root, level, res):
        if root == None:
            
            return res
        
        if len(res) < level:
            print(level)
            res.append([root.val])
            
        else:
            res[level - 1].append(root.val)
        
        res = self.preorder(root.left, level + 1, res)
        res = self.preorder(root.right, level + 1, res)
        
        return res
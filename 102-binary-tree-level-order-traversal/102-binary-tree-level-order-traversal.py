# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q = deque()
        lvl_order = []
        
        cur = root
        q.append([cur])
        lvl_order.append([cur.val])
   
        
        while q:
            cur = q.popleft()
            cur_lvl = []
            
            cur_nodes = []
            for num in cur:
                if num.left:
                    cur_lvl.append(num.left.val)
                    cur_nodes.append(num.left)
                if num.right:
                    cur_lvl.append(num.right.val)
                    cur_nodes.append(num.right)
            
            print(cur_lvl)
            if len(cur_lvl) > 0:
                q.append(cur_nodes)

                lvl_order.append(cur_lvl)
        
        return lvl_order
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        cur = head
        
        while cur:
            if cur.val in d:
                d[cur.val] += 1
                if d[cur.val] > 10:
                    return True
            else:
                d[cur.val] = 1
                
            cur = cur.next
        return False
            
        
        
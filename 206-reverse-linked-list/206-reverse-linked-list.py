# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None:
        #     return
        # if head.next is None:
        #     return head
        
        p = None
        c = head
        while c:
            t = c.next
            c.next = p
            p = c
            c = t
            
            
        return p
# prev = None
#             cur = head
#             while cur:
#                 nxt = cur.next
#                 cur.next = prev
#                 prev = cur
#                 cur = nxt


#             return prev
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
        
        p, c= None, head
        
        while c:
            t = c.next
            c.next = p
            p = c
            c = t
            
        return p

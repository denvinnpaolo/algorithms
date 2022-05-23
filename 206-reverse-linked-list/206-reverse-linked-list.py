# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return
        
        s = []
        
        reversedTail = head
        
        while reversedTail != None:
            s.append(reversedTail)
            reversedTail = reversedTail.next
            
        reversedTail = s.pop()
        head = reversedTail


        while len(s) != 0:
            p = s.pop()
            p.next = None
            reversedTail.next = p
            reversedTail = reversedTail.next
        
        return head

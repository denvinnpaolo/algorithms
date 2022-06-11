# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        start = head
        mid, end = head, head.next
        # get mid
        while end and end.next:
            mid = mid.next
            end = end.next.next
        
        end = mid.next
        mid.next = None
        
        # reverse end
        rev = None
        cur = end
        while cur:
            temp = cur.next
            cur.next = rev
            rev = cur
            cur = temp
            
            
        while start and rev:
            temp1 = start.next
            temp2 = rev.next
            
            start.next = rev
            rev.next = temp1
            
            rev = temp2
            
            start = temp1
            
            
        return head
            
        
        
            
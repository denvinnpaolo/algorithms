# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        nth = dummy
        end = head
        while n != 0 and end:
            end = end.next
            n -= 1
        
        
        while end:
            nth = nth.next
            end = end.next
            
        nth.next = nth.next.next
        
        return dummy.next
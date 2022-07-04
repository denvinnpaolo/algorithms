# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        front, back = dummy, head

        while back and n != 0:
            back = back.next
            n -= 1
        
        while back:
            front = front.next
            back = back.next
        
        front.next = front.next.next
        
        return dummy.next

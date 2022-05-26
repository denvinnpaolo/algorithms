# - linkedlist head
# - n represents the node in the list to be removed
# - n <= len(linkedList)
# - 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        front = dummy
        back = head
        
        while n > 0 and back:
            back = back.next
            n-=1
            
        while back:
            back = back.next
            front = front.next
            
        front.next = front.next.next
        return dummy.next
    
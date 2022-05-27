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
        
        back = dummy
        front = head
        
        while n > 0 and front:
            front = front.next
            n -= 1
            
        while front:
            back = back.next
            front = front.next
        
        back.next = back.next.next
        
        return dummy.next
    
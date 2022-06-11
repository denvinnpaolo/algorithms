# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        back = front = head
        
        while front and front.next:
            back = back.next
            front = front.next.next
                
            if back == front:
                return True
                
        return False
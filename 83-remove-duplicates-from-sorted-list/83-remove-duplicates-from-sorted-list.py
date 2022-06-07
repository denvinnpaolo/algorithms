# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next if cur.next.next else None
            else:
                cur = cur.next
        return head
                
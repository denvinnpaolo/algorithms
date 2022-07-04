# Will have a list with a length of 3
# each node will have a attribute point to the next list

# steps
# find the mid node
# l1 = head -> mid
# l2 = mid + 1 -> tail
# reverse l2 ex:  3 -> 4 = 4 ->
# merge l1 and l2 where l1 is the first node followed by head of l2
# continue until l1 and l2 == None

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
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        l1 = head
        mid = slow.next
        slow.next = None
        
        l2 = None
        
        while mid:
            temp = mid.next
            mid.next = l2
            l2 = mid
            mid = temp
        
        
        cur = l1
        
        while cur and l2:
            temp = cur.next
            cur.next = l2
            l2 = l2.next
            cur.next.next = temp
            
            cur = temp
        
        return l1
            
            
            
            
            
            
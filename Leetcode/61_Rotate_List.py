# Rotate Linked List

# Description:
# Given the head of a linked list, rotate the list to the right by k places.

# Constraints:
#   The number of nodes in the list is in the range [0, 500].
#   -100 <= Node.val <= 100
#   0 <= k <= 2 * 109

# Result
# Runtime: 44 ms, faster than 61.81% of Python3 online submissions for Multiply Strings.
# Memory Usage: 14.2 MB, less than 83.49% of Python3 online submissions for Multiply Strings.

# Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check if there's a list
        if head == None:
            return head
        # Make a list using the nodes to be able to find length of the list and the value of the new head
        a = self.getLengthAndVal(head)
        
        l = len(a)
        
        # refactor k if it's bigger than the length of the list
        if k > l:
            k %= l
        
        
        if k == 0 or l == 1 or l == k:
            return head
        
        # find new head    
        head = self.getNewHead(head, a[-k], k, l)
        
        return head
    
    
    
    def getNewHead(self, head, val, k ,l):
        newHeadVal = val
        
        tempHead = head
        count = 0
        
        # use count to get to the right node
        while count <= l -(k + 1):
            if count == l -(k + 1):
                # sets newHead as the next node
                newHead = tempHead.next
                # sets current node next as None (This will be the end of the new list)
                tempHead.next = None
                # get the new head all the way to the end of the list 
                tempHead = newHead
                while tempHead.next:
                    tempHead = tempHead.next
                # sets the end of the new head's next node as the left over nodes
                tempHead.next = head
                break
            else:
                count += 1
                tempHead = tempHead.next
        

        return newHead   
    
    # make an array out of the nodes using it's value
    def getLengthAndVal(self, head): 
        a = []
        while head:
            a.append(head.val)
            head = head.next
            
        return a
# 203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if head is None:
            return head
        
        curr = head
        
        while curr.next is not None:
            
            if curr.next.val ==val:
                curr.next = curr.next.next
            else:
                curr= curr.next
        
        if head:
            if head.val == val:
                head = head.next
                
        return head
        


# 206. Reverse Linked List

#Iterative Method

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next  
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev
            
        
# Recursive Method




class Solution:
    def reverseList(self, head):
        
        def recursion(prev, curr):
            if not curr:
                return prev
            
            tail = recursion(curr, curr.next)
            curr.next = prev
            
            return tail
        
        return recursion(None, head)



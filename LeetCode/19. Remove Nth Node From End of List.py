#19. Remove Nth Node From End of List

#method1 - One pass - O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # move currentNode n steps into list
        
        currentNode = head
        
        for i in range(n):
            currentNode = currentNode.next
        
        
        if currentNode == None:   # edge case
            return head.next
        # move both pointers untill currentNode reaches the end of the list
        
        nodeBeforeRemoved = head
        
        while currentNode.next != None:
            nodeBeforeRemoved = nodeBeforeRemoved.next
            currentNode = currentNode.next
            
        nodeBeforeRemoved.next = nodeBeforeRemoved.next.next
        
        return head
      
      
            
        

# Method 2- Two pass appraoch - O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        length = 0
        while curr is not None:
            length +=1
            curr = curr.next
        print(length)
        
        if length == n:     # edge case
            return head.next
        traverse_till  = length - n -1
        print(traverse_till)
        curr = head
        
        for i in range(traverse_till):
            curr = curr.next

        print(curr.val)
    
        curr.next = curr.next.next
        
        return head
        
      
            
        
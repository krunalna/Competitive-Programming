#21. Merge Two Sorted Lists

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
            
        curr = ListNode(-1)
        head = curr
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                node = ListNode(val = list1.val)
                curr.next = node
                list1 = list1.next
            
            else:  
                node = ListNode(val = list2.val)
                curr.next = node
                list2 = list2.next
                
            curr = curr.next
            
        if list1 is not None:
            curr.next = list1
        else:
            curr.next = list2
            
        return head.next
                
        
        
                
        
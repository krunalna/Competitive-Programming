# 1290. Convert Binary Number in a Linked List to Integer

# Steps : Traverse through the LL and append the values in list
# Reverse the list
# Traverse through the reverse list and convert them to integer

#Time Complexity - O(n)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        
        
        ct = 0
        num = 0
        curr = head
        temp = []
        
        while curr is not None:
            
            temp.append(curr.val)
            curr = curr.next
        temp.reverse()
        
        for idx, element in enumerate(temp):
            
            num = num + element*(2**idx)
        
        return num


    # Method2: 

    # generate a binary string by traversing throught the LL
    # convert that string to integer using inbuilt function int(s,2)

class Solution:
    def getDecimalValue(self, head):
        
        curr = head
        strr = ""
        while curr:
            strr += str(curr.val)
            curr = curr.next
        return int(strr,2)
    
        
        
            
        
        
        
            
            
       
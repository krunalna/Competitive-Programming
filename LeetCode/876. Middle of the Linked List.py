# 876. Middle of the Linked List


#method1 : Slow and Fast pointer approach


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
            
        return slow
            

#method 1: Find the length of LL by traversing
#Divide length by 2 and traverse till half.

#Time complexity = O(n)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
  
        
        temp=head # I dont want to make new changes to head so I created temp
        lengthOfLinkedList=0

        while temp!=None: # I find Lenght of linked List
            lengthOfLinkedList+=1
            temp=temp.next

        middleIndex=lengthOfLinkedList//2 #Find middle of LinkedList

        while middleIndex>0:   
            head=head.next
            print("head", head.val)
            print("middle", middleIndex)
            middleIndex-=1

        return head


#Method2 : 
    
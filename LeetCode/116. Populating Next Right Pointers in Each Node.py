#116. Populating Next Right Pointers in Each Node

# Classic example of level order traversing

#method1:
class Solution:
    
    def connect(self, root):
        if not root:
            return root
		# set the initial node to root
        node = root
		
		# first (outer) while loop, ends when node has no children (reaches the tree top)
        while node.left: 
		
		    # set pointer to the first node (left most) in the linked list
            n = node
			
			# second (inner) while loop, ends when pointer is None
            while n:
				
				# set left_child.next to right_child
                n.left.next = n.right
				
				# if pointer is not the right most node, set right_child.next to pointer.next.left_child
                if n.next:
                    n.right.next = n.next.left
					
				# after each loop, pointer is set to its next node in the linked list
                n=n.next
			
			# when inner while loop ends (reaches the right most node), return to outer while loop and set pointer node to its left child (start to connect next layer of nodes)
            node = node.left
		
        return root

#Method 2:  - Time complexity O(n) Space Complexity O(n)
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def level_order_traversal(self, root):
        
        if not root:
            return 
        
        queue = []
        queue.append(root)
        
        while queue:
            
            
            
            size = len(queue)
            
            for i in range(size):
                curr = queue.pop(0)
                print("Curr = " ,curr.val)
                print("Size = ", size)
                
                
                if i < size-1:
                    curr.next = queue[0]
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
         
        return root
        
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        return self.level_order_traversal(root)
        
        
        
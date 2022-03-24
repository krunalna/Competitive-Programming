#617. Merge Two Binary Trees

#Recursive Method - Time Complexity O(n) 

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            
            root1.val +=root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            
            return root1
        
            

#Method2 - Iterative

class Solution(object):
    def mergeTrees(self, root1, root2):
        
        if not (root1 or root2):
            return None
        root = TreeNode(0)
        stack = [(root, root1,root2)]
        
        while stack:
            node, n1, n2 = stack.pop()

            if n1 and n2:
                node.val = n1.val+n2.val
                if n1.left  or n2.left :
                    node.left = TreeNode(0)
                    stack.append((node.left,n1.left,n2.left))
                if n1.right  or n2.right :
                    node.right = TreeNode(0)
                    stack.append((node.right, n1.right,n2.right))
                    
            elif not n2:
                node.val = n1.val
                if n1.left:
                    node.left = TreeNode(0)
                    stack.append((node.left,n1.left,None))
                if n1.right:
                    node.right = TreeNode(0)
                    stack.append((node.right, n1.right,None))
            
            elif not n1 :
                node.val = n2.val
                if n2.left:
                    node.left = TreeNode(0) 
                    stack.append((node.left,None,n2.left))
                if n2.right:
                    node.right = TreeNode(0)
                    stack.append((node.right, None ,n2.right))
                    
        return root
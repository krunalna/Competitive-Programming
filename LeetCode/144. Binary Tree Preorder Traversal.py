#144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Iterative method

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    
        
    def preorderTraversal(self, root):
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            
            if node is not None:
                result.append(node.val)

                if node.right:
                    stack.append(node.right)    # first append right coz left should be on top of the stack to get printed
                    
                if node.left:
                    stack.append(node.left)

        return result
        
        
        
        

# Recursive Method - Time Complexity O(n)
class Solution(object):
    
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        
        
        """"
        
        res = []
        
        if root:
            res.append(root.val)
            res.extend(self.preorderTraversal(root.left))
            res.extend(self.preorderTraversal(root.right))
            
        return res
        
        """
    
        self.res = []
        
        def preOrder(node):
            
            if node is  None:
                return None
            
            self.res.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
            
        preOrder(root)
        
        return self.res
        
        
        

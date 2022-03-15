#112. Path Sum


#Iterative Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        if not root:
            return False
        
        total = targetSum-root.val
        
        stack = [(root, total)]
        
        while stack:
            
            curr_node, curr_total = stack.pop()
            
            if not curr_node.right and not curr_node.left and curr_total == 0:
                return True
            
            if curr_node.right:
                stack.append((curr_node.right, curr_total-curr_node.right.val))
            
            if curr_node.left:
                stack.append((curr_node.left, curr_total - curr_node.left.val))
                
        return False
        

#Recursive Solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        if not root:
            return False
        total = targetSum
        total  = total - root.val
        
        if not root.left and not root.right:
            return total ==  0
        
        return self.hasPathSum(root.left, total) or self.hasPathSum(root.right, total)
        
        
        
        
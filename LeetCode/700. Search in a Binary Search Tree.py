#700. Search in a Binary Search Tree


#Iterative approach

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        while root and root.val != val:
            
            if val < root.val:
                root = root.left
            else:
                root = root.right
            
        return root
            
        
        


#Recursive approach

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        if root is None:
            return None
            
        if root.val == val:
            return root
        
        if root.val < val:
             return self.searchBST(root.right, val)
        
        if root.val > val:
             return self.searchBST(root.left, val)
            
        return None
            
            
        
        
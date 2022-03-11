# 404. Sum of Left Leaves

#Recursion O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = 0
        
        if not root:
            return total
        
        if root.left and not root.left.left and not root.left.right:
            total+=root.left.val
            
        return total + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        
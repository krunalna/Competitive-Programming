# 98. Validate Binary Search Tree


#Recursive approach

#Initialise the left and right as max and min values possible. 
#The base case is that if the root is null, then True is returned
#We check 3 conditions simultaneously:-
# 1)  Check if root.val is greater than left and lesser than right
# 2) Recursively call the function , where for the recursive call of root.left, the parameter right is set to root.val
# 3) Recursively call the function , where for the recursive call of root.right, the parameter left is set to root.val

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        return valid(root, float('-inf'), float('inf'))

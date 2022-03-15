#145. Binary Tree Postorder Traversal145. Binary Tree Postorder Traversal

#Recursive Solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative 1: Following the left-right-node order

class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        stack, res = [root], []
        visited_left = set()
        visited_right = set()
        while stack:
            temp = stack[-1]
            while temp.left and temp not in visited_left:
                stack.append(temp.left)
                visited_left.add(temp)
                temp = temp.left
            if temp.right and temp not in visited_right:
                visited_right.add(temp)
                stack.append(temp.right)
                temp = temp.right
            else:
                temp = stack.pop()
                res.append(temp.val)
            
        return res

# method2 : Iterative - Similar to pre-order traversal

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return  []
        stack = [root,]
        result = []
        
        while stack:
            
            curr = stack.pop()
            
            result.append(curr.val)
            
            if curr.left:
                stack.append(curr.left)
                
            if curr.right:
                stack.append(curr.right)
                    
        return result[::-1]


# Recursive soultion
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        
        if root:
            res.extend(self.postorderTraversal(root.left))
            res.extend(self.postorderTraversal(root.right))
            res.append(root.val)
            
        return res
    
    
            


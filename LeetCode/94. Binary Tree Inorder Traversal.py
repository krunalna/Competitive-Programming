#94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        
        while root or stack:
            
            if root:
                stack.append(root)
                root = root.left
                
            else:
                
                root = stack.pop()
                result.append(root.val)
                root = root.right
            
        return result
        
        

# Recursive One-liner

class Solution:
    def inorderTraversal(self, root):
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


#recursive - DFS

class Solution:
    def inorderTraversal(self, root):
        def dfs(node, ans=[]):
            if node:
                dfs(node.left)
                ans.append(node.val)
                dfs(node.right)

            return ans

        return dfs(root)




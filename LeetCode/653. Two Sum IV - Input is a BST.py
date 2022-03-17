#653. Two Sum IV - Input is a BST


#recursive - using hashset
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
         
        def find(node, k , hashset):
            if node is None:
                return False
            
            complement = k - node.val
            
            if complement in hashset:
                return True
            
            hashset.add(node.val)
            
            return find(node.left, k, hashset) or find(node.right, k, hashset)
        
        
        hashset = set()
        
        return find(root,k,hashset)
       
        
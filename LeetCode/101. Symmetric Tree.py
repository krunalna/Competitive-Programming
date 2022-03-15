#101. Symmetric Tree

"""
The tree is supposed to be symmetric so the left subtree of the root should be a mirrored version of the right subtree of the root. Therefore, I create two queues for both subtrees which is a variation of standard BFS. Afterwards, in every iteration I first append the left child to the left queue and afterwards the right child to the left queue (standard order) and for the right queue I use the flipped order - first append right child and then left child. This way, if the tree is symmetric, the queues should contain the same values.

Now let's consider the edge cases.
If root has no children, we append None to both queues. Then we dequeue them and since they are both None, we continue to the next iteration. In the next iteration the queue is empty, so we return True.
If at some point, one of the dequeued node is None and the other one is not, we return False - the tree is not symmetric. We need a separate if statement because using node.val when node = None would raise an exception.
"""

# Iterative Approach

class Solution:
    def isSymmetric(self, root):
        left_queue = []
        right_queue = []
        left_queue.append(root.left)
        right_queue.append(root.right)
        while left_queue and right_queue:
            left_node = left_queue.pop(0)
            right_node = right_queue.pop(0)
            
            # if both nodes are None then we reached the leafs
            if left_node is None and right_node is None:
                continue
            
            # if only one of the nodes is None, then they are different
            if left_node is None or right_node is None:
                return False
            
            # if nodes have different values, the tree is noy symmetric
            if left_node.val != right_node.val:
                return False
            
            # flip the nodes order so that dequeued nodes have the same values
            # in a symmetric tree
            
            left_queue.append(left_node.left)
            right_queue.append(right_node.right)

            left_queue.append(left_node.right)
            right_queue.append(right_node.left)
        
        return True	


#Recursive Approach

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
    
    def isMirror(self, node1 ,node2):
        
        if node1 is None and node2 is None:
            return True
        
        if node1 is None or node2 is None:
            return False
        
        return (node1.val == node2.val ) and self.isMirror(node1.right, node2.left) and self.isMirror(node2.right, node1.left)
        

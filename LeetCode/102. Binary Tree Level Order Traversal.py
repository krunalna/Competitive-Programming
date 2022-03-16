#102. Binary Tree Level Order Traversal

#iterative approach:

"""
Let's keep nodes of each tree level in the queue structure, which typically orders elements in a FIFO (first-in-first-out) manner. In Java one could use LinkedList implementation of the Queue interface. In Python using Queue structure would be an overkill since it's designed for a safe exchange between multiple threads and hence requires locking which leads to a performance loose. In Python the queue implementation with a fast atomic append() and popleft() is deque.

The zero level contains only one node root. The algorithm is simple :

    Initiate queue with a root and start from the level number 0 : level = 0.

    While queue is not empty :

        Start the current level by adding an empty list into output structure levels.

        Compute how many elements should be on the current level : it's a queue length.

        Pop out all these elements from the queue and add them into the current level.

        Push their child nodes into the queue for the next level.

        Go to the next level level++.


"""

from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels

#recursive approach

"""
The simplest way to solve the problem is to use a recursion. Let's first ensure that the tree is not empty, and then call recursively the function helper(node, level), which takes the current node and its level as the arguments.

This function does the following :

    The output list here is called levels, and hence the current level is just a length of this list len(levels). Compare the number of a current level len(levels) with a node level level. If you're still on the previous level - add the new one by adding a new list into levels.

    Append the node value to the last list in levels.

    Process recursively child nodes if they are not None : helper(node.left / node.right, level + 1).

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        
        if root is None:
            return levels
            
        def helper(node, level):
            
            if len(levels) == level:
                levels.append([])
                
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
                
        helper(root, 0)
        
        return levels
        
# 589. N-ary Tree Preorder Traversal
#Useful link - https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/786364/Python-%2B-iterative-%2B-recursive-%2B-explanation
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#method1 - Recursive 

#time complexity - O(n) - Space Complexity  - O(n)
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        
        output = []
        
        def helper(node):
            
            if node is None:
                return 
            
            output.append(node.val)
            
            for i in node.children:
                
                c = helper(i)
         
        helper(root)
        return output

# Method 2 Iterative - DFS

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack = [root]
        output = []
        
        # Till there is element in stack the loop runs.
        while stack:
            
            #pop the last element from the stack and store it into temp.
            temp = stack.pop()
            
            # append. the value of temp to output
            output.append(temp.val)
            
            #add the children of the temp into the stack in reverse order.
            # children of 1 = [3,2,4], if not reveresed then 4 will be popped out first from the stack.
            # if reversed then stack = [4,2,3]. Here 3 will pop out first.
            # This continues till the stack is empty.
            stack.extend(temp.children[::-1])
        
        #return the output
        return output
        
# 74. Search a 2D Matrix

# Time complexity - O(n)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        for i in range(len(matrix)-1):
            if (target >= matrix[i][0]) and (target < matrix[i+1][0]):
                row = i
            else:
                if target >= matrix[len(matrix)-1][0]:
                    row = len(matrix)-1
                    
        return target in matrix[row]
        
                
  
                
# method2 - Binary Search - Time Complexity  O(mn)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        
        if m == 0:
            return False
        
        n = len(matrix[0])
        
        left, right = 0, m* n -1
        
        while left <= right:
            pivot_index = (left+right)//2
            row = pivot_index //n
            col = pivot_index %n
            pivot_element = matrix[row][col]
            
            if target == pivot_element:
                return True
            
            else:
                if target < pivot_element:
                    right = pivot_index-1
                else:
                    left = pivot_index +1
                    
        return False
        
                
  
                
        
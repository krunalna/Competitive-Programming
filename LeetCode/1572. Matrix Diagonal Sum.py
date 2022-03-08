# 1572. Matrix Diagonal Sum

#Method1 - Brute Force -  Time complexity - O(n^2)

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows=  len(mat)
        cols = len(mat[0])
        total = 0
        for i in range(rows):
            for j in range(cols):
                
                if i==j or i+j == (rows-1):
                    total +=mat[i][j]
                
        return total
        
                
#method 2 - Single pass - Time Complexity - O(n)

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows=  len(mat)
        cols = len(mat[0])
        total = 0
        
        
        for index in range(rows):
            total += mat[index][index]      # forward diagonal - i ==j
            total += mat[index][rows-1-index]   # backward diagonal 
            
        if rows %2==0:
            return total
        else:
            return total-mat[rows//2][rows//2]   #subtract the single repeating diagonal element
        
        
                
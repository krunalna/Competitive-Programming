#48. Rotate Image


#method 1: 

class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
		# iterate through matrix
        for i in range(n):
            for j in range(i,n):
			
			    # transpose the matrix, turning rows into columns and vice versa
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
			
			# reverse the resulting rows
            matrix[i].reverse()
            

#method2:

class Solution(object):
    
    #taking transpose of the matrix
    def transpose (self, matrix):
        n = len(matrix)
        
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
                
    #reverse the matrix
    def reverse(self, matrix):
        
        n = len(matrix)
        
        for i in range(n):
            for j in range(n//2):
                
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        self.transpose(matrix)    # take transpose
        self.reverse(matrix)        # reverse the transposed matrix
        

#542. 01 Matrix

class Solution:
    def updateMatrix(self, mat):
        
        rows = len(mat)     # get number of rows
        cols = len(mat[0])  # get number of cols
         
        queue = []             #maitain a queue
        
        for i in range(rows):       # traverse through the matrix - if we encounter 0 - added it to the queue
            for j in range(cols):   # else mark '1' with some symbol to identify later
                
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = "*"
                    
        neighbours = [(1,0),(-1,0), (0,1),(0,-1)]   # declaring neighbours
        
        for row, col in queue:                    #traverse through queue
            for dr,dc in neighbours:                # for each element of queue - traverse its 4 neighbours
                
                newrow = row + dr
                newcol = col + dc
                
                if 0<=newrow<rows and 0<=newcol<cols and mat[newrow][newcol] == "*":   # if newrow and newcol are within limits and are that special symbol
                                                                                    # make its value = 1+ mat[row][col] ie from original i,j and append the newrowand new col to queu for travesing

                    mat[newrow][newcol] = mat[row][col] +1
                    queue.append((newrow, newcol))
                    
                    
        return mat
        
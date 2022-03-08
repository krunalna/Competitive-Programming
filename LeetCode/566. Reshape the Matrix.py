# 566. Reshape the Matrix

#Method1 - Convert given matrix to 1-D array and then make a resul
#resultant matrix with required r and c 
# time complexity - O(n^2) or O(m.n)

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        one_d =  []
        
        rows = len(mat)
        cols = len(mat[0])
        
        if rows*cols != r*c:
            return mat
        
        for i in range(rows):
            for j in range(cols):
                
                one_d.append(mat[i][j])
                
        #print(one_d)
        res = []
        '''
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(one_d.pop(0))
            res.append(temp)

        '''

        for i in range(0,len(one_d),c):
            res.append(one_d[i:i+c])
            
        return res
    

    #method2 - using div mod operator

    '''
    Do you know how a 2-D array is stored in the main memory(which is 1-D in nature)?
    It is internally represented as a 1-D array only. The element nums[i][j]nums[i][j]nums[i][j]
    of numsnumsnums array is represented in the form of a one dimensional array by using the
    index in the form: nums[n∗i+j]nums[n*i + j]nums[n∗i+j], where nnn is the number of columns 
    in the given matrix. Looking at the same in the reverse order, while putting the elements in the elements in the
    resultant matrix, we can make use of a countcountcount variable which gets incremented for every element traversed
    as if we are putting the elements in a 1-D resultant array. But, to convert the countcountcount back
    into 2-D matrix indices with a column count of ccc, we can obtain the indices as
     res[count/c][count%c]res[count/c][count\%c]res[count/c][count%c]
      where count/ccount/ccount/c is the row number and count%ccount\%ccount%c is the coloumn number.
       Thus, we can save the extra checking required at each step.

    
class Solution:
	def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        if r*c != m*n:
            return mat

        reshaped = [[0]*c for _ in range(r)]
        for N in range(r*c):
            i, j = divmod(N, c)
            mati, matj = divmod(N, n)
            reshaped[i][j] = mat[mati][matj]
        return reshaped

'''

        
                
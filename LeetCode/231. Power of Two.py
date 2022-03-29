# 231. Power of Two

class Solution(object):
    
  
        
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
       """
        """
        
        if n == 0:
            return False
        
        while n%2 == 0:
            n /=2
        
        return n == 1
        
        """
        
        #Method2 : Count the number of set bits: if count ==1 return True else False
        # if the integer is power of 2 then it will only contain one set bit
        
        count = 0
        
        while n>0:
            count+=1
            n = n & (n-1)
            
        if count == 1:
            return True
        else:
            return False
        
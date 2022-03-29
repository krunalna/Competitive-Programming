#191. Number of 1 Bits

#method 1 - counting bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        
        while n >0:
            count+=1
            n =  n & (n-1)
            
        return count

#method 2: counting bits -2


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        
        while n>0:
            if n & 1 >0:
                count+=1
            n=n>>1
        
        return count

#method 3: using inbuilt counter

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return bin(n)[2:].count('1')
        
# 1356. Sort Integers by The Number of 1 Bits

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        arr.sort()      # sorting the array so that if all the elements contain 1 bit, they are returned in sorted order
        def countbits(n):   # count bits
            count = 0
            
            while n > 0:
                n = n & (n-1)
                count +=1
                
            return count
        
        countlist = []
        
        for num in arr:    
            countlist.append([num, countbits(num)])
        
        #print(countlist)
        
        countlist.sort(key = lambda x : x[1])   # sorting on basis of bit count
        
        #print(countlist)
        
        result = []
        
        for num, bits in countlist:
            result.append(num)
            
        return result
        
        
        
      
        
        
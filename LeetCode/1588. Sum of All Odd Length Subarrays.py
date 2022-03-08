# 1588. Sum of All Odd Length Subarrays

#time complexity - O(n^2)

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total = sum(arr)
        
        length = len(arr)
        
        for i in range(3, length+1, 2):
            for j in range(length):
                if i+j > length:
                    break
                    
                total += sum(arr[j:i+j])
                
        
        return total
        
        
        
# Dp Approach - https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/854192/Python-and-C%2B%2B-Easy-solution-Prefix-sum-approach-(DP)


class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        total = 0
        length = len(arr)
        
        prefix_sum = [0]*length
        
        prefix_sum[0] = arr[0]
        
        for i in range(1,length):
            prefix_sum[i] = arr[i] + prefix_sum[i-1]
            
        subsize = 3
        total += prefix_sum[length-1]
        
        while subsize<=length:
            for start in range(0, length-subsize+1):
                end = start + subsize-1
                if start!=0:
                    total += prefix_sum[end] - prefix_sum[start-1]
                    
                else:
                    total += prefix_sum[end]
            
            subsize +=2
            
        return total
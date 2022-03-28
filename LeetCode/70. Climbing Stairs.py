# 70. Climbing Stairs

#method1  Dp approach

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 1
        
        dp =[0,1,2]
        
        for i in range(3, n+1):
            dp.append(dp[i-1]+dp[i-2])
            
        return dp[n]
        

#Method2 - Fibonacci series formula - 

import math

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        sqrt5  = math.sqrt(5)
        
        numerator = math.pow( (1+sqrt5)/2, n+1) - math.pow((1-sqrt5)/2, n+1)
        
        return (int)(numerator/sqrt5)
        
        

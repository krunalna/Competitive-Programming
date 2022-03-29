#342. Power of Four


#method 1 - O(logn)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 0:
            return False
        
        while n % 4 ==0:
            n = n/4
            
        return n ==1
            
        
            
    #method2 - O(n)

class Powers:
    def __init__(self):
        max_power = 15
        self.nums = nums = [1] * (max_power + 1)
        for i in range(1, max_power + 1):
            nums[i] = 4 * nums[i - 1]

class Solution:
    p = Powers()
    def isPowerOfFour(self, num: int) -> bool:
        return num in self.p.nums
            
        
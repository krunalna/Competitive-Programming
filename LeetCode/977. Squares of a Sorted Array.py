#977. Squares of a Sorted Array

# Method1 - Two pointer - time complexity O(n)

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        
        for i in range(n-1, -1, -1):
            
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right = right-1
                
            else:
                square = nums[left]
                left = left+1
                
            result[i] = square * square
            
        return result
        

# method 2 - Square and sort - Time complexity O(nlogn)

class Solution:
    def sortedSquares(self, nums):
        squares = []
        
        for num in nums:
            squares.append(num*num)
            
        return sorted(squares)
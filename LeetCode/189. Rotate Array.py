#189. Rotate Array


#Optimal appraoch - O(n)


class Solution(object):
    
    def reverse( self,nums, start, end):
        
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start = start+1
            end = end-1
            
            
        
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        print(k)
        k = k%n
        print(k)
        
        self.reverse(nums, 0, n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums, k, n-1)
            
        
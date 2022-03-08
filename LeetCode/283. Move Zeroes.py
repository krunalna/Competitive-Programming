#283. Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
     
        length = len(nums)
     
        for i in range(len(nums)):
            k = length - i-1
            if nums[k] == 0:
               
                nums.pop(k)
                nums.append(0)
                
        
            
#Method 2  - Time complexity O(n)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
     
        n = len(nums)
        ptr = 0
        count = 0
        
        while ptr <n:
            
            if nums[ptr] == 0:
                count +=1
                nums.pop(ptr)
                n = n-1

            else:
                ptr+=1
                
        nums.extend([0]*count)
        
            
# method 3 - Two Pointer Approach

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Idea: have a slow pointer pointing at the beginning and only move with condition.
        # Condition: when iterating nums, if we encounter a nonzero, swap places with the slow and increase slow by 1.
        slow = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow+=1

#136. Single Number

#method 1 - Math - O(n)

#   2∗(a+b+c)−(a+a+b+b+c)=c
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        return 2 * sum(set(nums)) - sum(nums)
        




#method2 = hashmap , Time complexity - O(n)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        
        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1
        
        for item, value in hashmap.items():
            
            if value == 1:
                return item
        

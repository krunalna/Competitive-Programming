# 303. Range Sum Query - Immutable

#using prefix sum method

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = []
        self.prefix_sum.append(nums[0])
        total = nums[0]
        for i in range(1,len(nums)):
            total = total+nums[i]
            self.prefix_sum.append(total)
            
        #print(self.prefix_sum)
        
        
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right]- self.prefix_sum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)